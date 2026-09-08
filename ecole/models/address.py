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
    id: Optional[int] = field(default=None, init=False)
    street: str
    city: str
    postal_code: int

    def __str__(self) -> str:
        return f"{self.street}, {self.postal_code} {self.city}"
