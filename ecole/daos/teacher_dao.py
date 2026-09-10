# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""

from models import address, teacher
from models.address import Address
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any

from models.teacher import Teacher


@dataclass
class TeacherDao(Dao[Teacher]):
    def create(self, teacher: Teacher) -> int:
        """Crée en BD l'entité Teacher correspondant au teacher Teacher

        :param teacher: à créer sous forme d'entité Teacher BD
        :return: le nombre de lignes modifiées par la requête d'insertion en BD (0 si la création a échouée)
        """

        teacher.id = int(self.init_counter("id_teacher", "Max_Id_Teacher", "teacher"))
        values_param: tuple = (teacher.id, teacher.hiring_date)
        table_params: list[str] = ["id_teacher", "hiring_date"]
        table_name: str = "teacher"

        return self.insert(table_name, table_params, values_param)

    def read(self, id_teacher: int) -> Optional[Teacher]:
        """Renvoit le teacher correspondant à l'entité dont l'id est id_teacher
                   (ou None s'il n'a pu être trouvé)"""
        course: Optional[Teacher]

        table_name: str = "teacher"
        id_name: str = "id_teacher"
        id_value: int = id_teacher

        return self.read_one(id_name, table_name, id_value)

    def update(self, teacher: Teacher) -> bool:
        """Met à jour en BD l'entité correspondant à obj, pour y correspondre

        :param obj: objet déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        table_name: str = "teacher"
        data_dict: dict = {
            "id_teacher": teacher.id,
            "hiring_date": teacher.hiring_date,
        }
        id_name: str = "id_course"
        id_value: int = teacher.id

        return self.modify(table_name, data_dict, id_name, id_value)
