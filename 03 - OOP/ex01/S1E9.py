from abc import ABC, abstractmethod


class Character(ABC):
    """A character from Game of Thrones"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a character with first name and alive status"""
        try:
            if not isinstance(first_name, str):
                raise TypeError("first_name must be a string")
            if not first_name.strip():
                raise ValueError("first_name cannot be empty")
            if not isinstance(is_alive, bool):
                raise TypeError("is_alive must be a boolean")

            self.first_name = first_name
            self.is_alive = is_alive

        except (TypeError, ValueError) as e:
            print(f"Error creating character: {e}")
            raise

    @abstractmethod
    def die(self):
        """Kill the character - must be implemented in subclasses"""
        pass


class Stark(Character):
    """A member of the Stark family"""

    def die(self):
        """Kill the Stark character"""
        try:
            if not hasattr(self, 'is_alive'):
                raise AttributeError("Missing is_alive attribute")

            was_alive = self.is_alive
            self.is_alive = False

            if not was_alive:
                print(f"{self.first_name} is already dead!")

        except AttributeError as e:
            print(f"Error in die method: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error in die method: {e}")
            raise
