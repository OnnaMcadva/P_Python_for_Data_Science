import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character lowercase ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Dataclass representing a student."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Generates login and random ID automatically."""
        self.login = f"{self.name[0].upper()}{self.surname}".capitalize()
        self.id = generate_id()
