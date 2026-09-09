#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de test de dao address
"""

from daos.address_dao import AddressDao
from models.address import Address
from typing import Optional


def main():
    print("Debut test address_dao")
    taille_de_la_table: int = 0
    result: int = 0

    address_dao = AddressDao()

    print(f"Test id max table address : {address_dao.init_counter("id_address", "Max_Id_Address", "address")}")
    print(f"Test de read_all_table: {address_dao.read_table()}")
    address_instance: Address = Address('1 place du Capitole', 'Toulouse', '31040')

    print("Test creation d'une address avec la méthode dao ")
    new_id: int = address_dao.create(address_instance)
    address_instance.id = new_id
    print(f"L'addresse inséré à pour id:{address_instance.id}")
    print("Test lecture d'une address avec la méthode dao ")
    print(address_instance)
    address_read: Optional[Address] = address_dao.read(address_instance)
    print("Lecture de l'élément précédemment créé :\n%s" % address_read)
    print("Test Update d'une address avec la méthode dao ")
    # On prépare l'objet Address avec ses nouvelles valeurs
    address_instance.id_address = new_id
    address_instance.street = '1 place du Capitole'
    address_instance.city = 'Toulouse'
    address_instance.postal_code = '31000'

    # On passe l'objet unique à la méthode DAO
    if address_dao.update(address_instance):
        print("La mise à jour s'est effectuée avec succès")
    else:
        print("Problème de mise à jour")
    print("Test delete d'une address avec la méthode dao ")
    if address_dao.delete(address_instance):
        print("la Suppression s'est effectuée avec succès")
    else:
        print("Problème de suppression")

    print("Fin test address_dao")

if __name__ == '__main__':
    main()