#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de test de dao course
"""
from daos.course_dao import CourseDao
from models.course import Course
from typing import Optional


def main():
    print("Debut test address_dao")
    taille_de_la_table: int = 0
    result: int = 0

    course_dao = CourseDao()

    print(f"Test id max table course : {course_dao.init_counter("id_course", "Max_Id_Course", "course")}")
    print(f"Test de read_all_table: {course_dao.read_table()}")
    course_instance: Course = Course('Musique', '2026-06-22', '2026-12-31', 6)

    print("Test creation d'une address avec la méthode dao ")
    new_id: int = course_dao.create(course_instance)
    course_instance.id = new_id
    print(f"L'addresse inséré à pour id:{course_instance.id}")
    print("Test lecture d'une address avec la méthode dao ")
    print(course_instance)
    address_read: Optional[Course] = course_dao.read(course_instance)
    print("Lecture de l'élément précédemment créé :\n%s" % address_read)
    print("Test Update d'une address avec la méthode dao ")
    # On prépare l'objet Course avec ses nouvelles valeurs
    course_instance.id_address = new_id
    course_instance.street = '1 place du Capitole'
    course_instance.city = 'Toulouse'
    course_instance.postal_code = '31000'

    # On passe l'objet unique à la méthode DAO
    if course_dao.update(course_instance):
        print("La mise à jour s'est effectuée avec succès")
    else:
        print("Problème de mise à jour")
    print("Test delete d'une address avec la méthode dao ")
    if course_dao.delete(course_instance):
        print("la Suppression s'est effectuée avec succès")
    else:
        print("Problème de suppression")

    print("Fin test address_dao")

if __name__ == '__main__':
    main()