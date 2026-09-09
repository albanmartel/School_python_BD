# -*- coding: utf-8 -*-

"""
Classe Address
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Address:
    """Adresse d'une personne (enseignant ou élève) :
    - id          : clé primaire de l'entité persistante
    - street      : rue de l'adresse
    - city        : ville
    - postal_code : code postal
    """
    street: str
    city: str
    postal_code: str
    id: Optional[int] = None

    def __str__(self) -> str:
        str_message: str = f"{self.street}, {self.postal_code} {self.city}"
        if self.id is not None:
            str_message += f", {self.id}"
        else:
            str_message += f", {0}"

        return str_message
