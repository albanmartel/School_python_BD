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
        pass



