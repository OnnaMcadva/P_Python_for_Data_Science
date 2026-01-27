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
    _login: str = field(init=False, repr=False)
    _id: str = field(init=False, repr=False)

    def __post_init__(self):
        """Generates login and random ID automatically."""
        if self.surname:
            self._login = f"{self.name[0].upper()}{self.surname}".capitalize()
        else:
            self._login = f"{self.name[0].upper()}"
        self._id = generate_id()

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        raise AttributeError("login is read-only and cannot be set")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        raise AttributeError("id is read-only and cannot be set")
