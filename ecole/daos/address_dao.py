# -*- coding: utf-8 -*-

"""
Classe Dao[Address]
"""

from models import address
from models.address import Address
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class AddressDao(Dao[Address]):
    def create(self, address: Address) -> int:
        """Crée en BD l'entité Address correspondant à l'adresse address

        :param address: à créer sous forme d'entité Address en BD
        :return: le nombre de lignes modifiées par la requête d'insertion en BD (0 si la création a échoué)
        """
        address.id = int(self.init_counter("id_address", "Max_id_address", "address")) + 1

        sql = "INSERT INTO address (id_address, street, city, postal_code) VALUES (%s, %s, %s, %s)"
        params = (address.id, address.street, address.city, address.postal_code)

        new_id: int = 0

        with Dao.connection.cursor() as cursor:

            cursor.execute(sql, params)
            new_id: int = cursor.lastrowid

        Dao.connection.commit()

        return new_id

    def read(self, address: Address) -> Optional[Address]:
        """Renvoit l'objet correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)

        :return un dictionnaire de la ligne concernée
        """
        return self.read_one("id_address", "address", address.id)

    def update(self, address: Address) -> bool:
        """Met à jour en BD l'entité correspondant à obj, pour y correspondre

        :param obj: objet déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        sql = "UPDATE address SET street = %s, city = %s, postal_code = %s WHERE id_address = %s"
        params = (address.street, address.city, address.postal_code, address.id)

        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, params)
            rowcount = cursor.rowcount

        Dao.connection.commit()

        return rowcount > 0


    def delete(self, address: Address) -> bool:
        """Supprime en BD l'entité correspondant à obj

        :param obj: objet dont l'entité correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """

        return self.delete_in_table("address", "id_address", address.id)

    def read_table(self) -> list[dict[str, Any]]:
        """
        Renvoit une liste d'objets à tous les enregistrements d'une entité
        (ou None s'il n'a pu être trouvé)

        :return: liste de dictionnaires de la table Address
        """
        return self.read_all_table("address")


if __name__ == '__main__':
    obj: AddressDao = AddressDao()

