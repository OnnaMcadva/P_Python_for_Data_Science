import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random 15-character lowercase string for student ID.
    Returns:
        str: A random string of 15 lowercase letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


# @dataclass(frozen=True) for all fields read-only, but we want only some to be read-only
@dataclass
class Student:
    """
    Dataclass representing a student with auto-generated login and ID.
    The login and id fields are read-only after creation.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False, repr=True)
    id: str = field(init=False, repr=True)

    def __post_init__(self):
        """
        Initialize login and id fields after object creation.
        Login is the first letter of the name (uppercase) plus the surname (lowercase),
        or just the first letter of the name with an alien emoji if surname is empty.
        ID is a random 15-character string.
        """
        if self.surname:
            self.login = self.name[0].upper() + self.surname.lower()
        else:
            self.login = self.name[0].upper() + "👽"
        self.id = generate_id()

    def __setattr__(self, key, value):
        """
        Prevent modification of login and id fields after creation.
        """
        if hasattr(self, key) and key in ("login", "id"):
            raise AttributeError(f"{key} is read-only and cannot be set")
        super().__setattr__(key, value)
