# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from models.course import Course
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> int:
        """Crée en BD l'entité Course correspondant au cours course

        :param course: à créer sous forme d'entité Course en BD
        :return: le nombre de lignes modifiées par la requête d'insertion en BD (0 si la création a échouée)
        """

        course.id = int(self.init_counter("id_course", "Max_Id_Course", "course"))
        print(f"course max id: {course.id}")
        values_param: tuple = (course.id, course.name, course.start_date, course.end_date, course.teacher)
        table_params: list[str] = ["id_course", "name", "start_date", "end_date", "id_teacher"]
        table_name: str = "course"

        return self.insert(table_name, table_params, values_param)

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        course: Optional[Course]
        
        table_name: str = "course"
        id_name: str = "id_course"
        id_value: int = id_course

        return self.read_one(id_name, table_name, id_value)

    def update(self, course: Course) -> bool:
        """Met à jour en BD l'entité correspondant à obj, pour y correspondre

        :param obj: objet déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        table_name: str = "course"
        data_dict: dict = {
            "name": course.name,
            "start_date": course.start_date,
            "end_date": course.end_date,
        }
        id_name: str = "id_course"
        id_value: int = course.id

        return self.modify(table_name, data_dict, id_name, id_value)

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité correspondant à obj

        :param obj: objet dont l'entité correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        table_name:str = "course"
        id_name: str = "id_course"
        id_value: int = course.id

        return self.delete_in_table(table_name, id_name, id_value)

    def read_table(self) -> list[dict[str, Any]]:
        """
        Renvoit une liste d'objets à tous les enregistrements d'une entité
        (ou None s'il n'a pu être trouvé)

        :return: liste de dictionnaires de la table Course
        """
        return self.read_all_table("course")
