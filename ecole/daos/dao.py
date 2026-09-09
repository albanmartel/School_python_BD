# -*- coding: utf-8 -*-

"""
Classe abstraite générique Dao[T], dont hérite les classes de DAO de chaque entité
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar, Optional
import pymysql.cursors


@dataclass
class Dao[T](ABC):
    connection: ClassVar[pymysql.Connection] = \
        pymysql.connect(host='localhost',
                        user='ecole',
                        password='FqDEuKWd9TxLERZg6ooh',
                        database='ecole',
                        cursorclass=pymysql.cursors.DictCursor)

    def init_counter(self, table_id: str, max_alias: str, table_name: str) -> int:
        """
        retourne la valeur maximale d'id dans la table

        :param table_id: identifiant unique de la table
        :param max_alias: alias du nombre de l'id de la table
        :param table_name: nom de la table
        """

        number: int = 0

        sql = "SELECT COALESCE(MAX(%s), 0) AS %s FROM %s"
        params = (table_id, max_alias, table_name)
        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, params)
            record = cursor.fetchone()

        if record is not None:
            number = record[max_alias]

        return number
        
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

    @abstractmethod
    def count(self) -> int:
        """ Compte le nombre de lignes d'une table

        :return: Le nombre de lignes d'une table.
        """
        ...
