# -*- coding: utf-8 -*-

"""
Classe Dao[Address]
"""
from email.headerregistry import Address

from models.address import Address
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class AddressDao(Dao[Address]):
    def read(self, id_address: int) -> Optional[Address]:
        address: Optional[Address]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM address WHERE id_address = %s"
            cursor.execute(sql, (id_address,))
            record = cursor.fetchone()
            if record is not None:
                address = Address(record['street'], record['postal_code'], record['city'])
                address.id = record['id_address']
            else:
                address = None

        return address

    def delete(self, address: Address) -> bool:
        pass

    def update(self, address: Address) -> bool:
        pass

    def create(self, address: Address) -> int:
        """Crée en BD l'entité Address correspondant à l'adresse address

        :param address: à créer sous forme d'entité Address en BD
        :return: le nombre de lignes modifiées par la requête d'insertion en BD (0 si la création a échouée)
        """

        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO address (street, city, postal_code) VALUES (%s, %s, %s)"
            cursor.execute(sql, address.__getattribute__('street'), address.__getattribute__('city'). address.__getattribute__('postal_code'))
            rowcount = cursor.rowcount

        Dao.connection.commit()

        return rowcount



