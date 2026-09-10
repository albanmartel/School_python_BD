# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""

from models import address
from models.address import Address
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any

from models.teacher import Teacher


@dataclass
class TeacherDao(Dao[Teacher]):
    def create(self, teacher: Teacher) -> int:
        """Crée en BD l'entité Teacher correspondant au teacher Teacher

        :param teacher: à créer sous forme d'entité Course en BD
        :return: le nombre de lignes modifiées par la requête d'insertion en BD (0 si la création a échouée)
        """

        teacher.id = int(self.init_counter("id_teacher", "Max_Id_Teacher", "teacher"))
        values_param: tuple = (teacher.id, teacher.hiring_date, teacher.id)
        table_params: list[str] = ["id_teacher", "hiring_date", "id_person"]
        table_name: str = "teacher"

        return self.insert(table_name, table_params, values_param)
