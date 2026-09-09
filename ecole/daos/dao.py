# -*- coding: utf-8 -*-

"""
Classe abstraite générique Dao[T], dont hérite les classes de DAO de chaque entité
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar, Optional, Any
import pymysql.cursors


@dataclass
class Dao[T](ABC):
    connection: ClassVar[pymysql.Connection] = \
        pymysql.connect(host='localhost',
                        user='ecole',
                        password='FqDEuKWd9TxLERZg6ooh',
                        database='ecole',
                        cursorclass=pymysql.cursors.DictCursor)

    def init_counter(self, id_name: str, max_alias: str, table_name: str) -> int:
        """
        retourne la valeur maximale d'id dans la table

        :param id_name: identifiant unique de la table
        :param max_alias: alias du nombre de l'id de la table
        :param table_name: nom de la table
        """

        number: int = 0

        sql = f"SELECT COALESCE(MAX({id_name}), 0) AS {max_alias} FROM {table_name}"
        with Dao.connection.cursor() as cursor:
            cursor.execute(sql)
            record = cursor.fetchone()

        if record is not None:
            # 1. Record est il un dictionnaire
            if isinstance(record, dict):
                number = record[max_alias]
            # 2. Record n'est pas un dictionnaire
            else:
                number = record[0]

        return int(number)

    def read_all_table(self, table_name) -> list[dict[str, Any]]:
        """
        Renvoit une liste d'objets à tous les enregistrements d'une entité
        (ou None s'il n'a pu être trouvé)
        :param table_name: nom de la table
        """

        sql = f"SELECT * FROM {table_name}"
        record_list: list[dict[str, Any]] = []
        columns= []

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql)
            records = cursor.fetchall()

            if cursor.description is not None:
                for col in cursor.description:
                    # Note : le nom du champ est au début
                    columns.append(col[0])

        if records:
            for record in records:
                # CAS 1 : Le curseur renvoie DÉJÀ un dictionnaire
                if isinstance(record, dict):
                    record_list.append(record)

                # CAS 2 : Le curseur renvoie un tuple
                elif len(columns) > 0:
                    record_dict = {}
                    for i in range(len(columns)):
                        field = columns[i]
                        value = record[i]
                        record_dict[field] = value

                    record_list.append(record_dict)
        
        return record_list

    def read_one(self, id_name: str, table_name: str, table_id: int) -> dict[str, Any]:
        """
        Renvoit l'objet correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)

        :param id_name: nom de l'identifiant de la table
        :param table_name: nom de la table
        :param table_id: numero de l'identifiant à lire

        :return: un dictionnaire de la ligne concernée
        """
        sql = f"SELECT * FROM {table_name} WHERE {id_name} = %s"
        param = table_id
        record_dict: dict[str, Any] = {}
        columns = []

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(sql, param)
                record = cursor.fetchone()

                if cursor.description is not None:
                    for col in cursor.description:
                        # Note : le nom du champs est au début
                        columns.append(col[0])

            if record is not None:
                # CAS 1 : Le curseur renvoie DÉJÀ un dictionnaire
                if isinstance(record, dict):
                    record_dict = record
                else :
                    # CAS 2 : Le curseur renvoie un tuple
                    if len(columns) > 0:
                        record_dict = {}
                        for i in range(len(columns)):
                            field = columns[i]
                            value = record[i]
                            record_dict[field] = value
        except Exception as e:
            print(f"Une exception s'est produite : {e}")

        return record_dict

    def delete_in_table(self, table_name: str, id_name:str, id_table: int ) -> bool:
        """Supprime en BD l'entité correspondant à id de table

        :param id_name: nom de l'identifiant dans la table
        :param id_table: l'id de la ligne à supprimer
        :param table_name: le nom de la table concernée par la suppression de ligne
        
        :return: True si la suppression a pu se réaliser
        """

        sql = f"DELETE FROM {table_name} WHERE {id_name} = %s"
        param = id_table

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(sql, param)
                rowcount = cursor.rowcount
            Dao.connection.commit()

            # si le nombre de ligne(s) supprimée(s) est superieur à zéro
            return rowcount > 0

        except Exception as e:
            Dao.connection.rollback()
            print(f"Une exception s'est produite : {e}")

            return False

    def insert(self, table_name: str, table_params: list[str], values_params: tuple) -> int:
        """
        Méthode générique pour l'insertion, une partie de la requête est paramétrée
        pour plus de sécurité.
        Si une exception a lieu elle est levée et affichée la valeur de zéro est renvoyée
        cela permet d'informer que la requête a échoué

        :param table_name:
        :param table_params:
        :param values_params:
        :return: un entier soit l'id inséré soit 0 (échec)
        """

        params_str = ", ".join(table_params)
        placeholders = ", ".join(["%s"] * len(values_params))

        sql = f"INSERT INTO {table_name} ({params_str}) VALUES ({placeholders})"

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(sql, values_params)
                new_id: int = cursor.lastrowid
            Dao.connection.commit()

            return new_id

        except Exception as e:
            Dao.connection.rollback()
            print(f"Une exception s'est produite : {e}")

            return 0

    @abstractmethod
    def create(self, obj: T) -> int:
        """Crée l'entité en BD correspondant à l'objet obj

        :param obj: à créer sous forme d'entité en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...

    @abstractmethod
    def read(self, id_entity: int) -> Optional[T]:
        """Renvoit l'objet correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        ...

    @abstractmethod
    def update(self, obj: T) -> bool:
        """Met à jour en BD l'entité correspondant à obj, pour y correspondre

        :param obj: objet déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...

    @abstractmethod
    def delete(self, obj: T) -> bool:
        """Supprime en BD l'entité correspondant à obj

        :param obj: objet dont l'entité correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
