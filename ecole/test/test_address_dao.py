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

    taille_de_la_table = address_dao.count()
    print("table a %s élément(s) avant la création d'une nouvelle adresse" % taille_de_la_table)

    address_instance: Address = Address('1 place du Capitole', 'Toulouse', '31040')

    print("Test creation d'une address avec la méthode dao ")
    new_id: int = address_dao.create(address_instance)
    print("%s élément(s) a été ajouté à la table" % (address_dao.count() - taille_de_la_table))
    print("Test lecture d'une address avec la méthode dao ")
    address_instance: Optional[Address] = address_dao.read(new_id)
    print("Lecture de l'élément précédemment créé :\n%s" % address_instance)
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