from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King Joffrey Baratheon/Lannister"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the king"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self._eyes = "brown"
        self._hairs = "dark"

    @property
    def eyes(self):
        """Get the king's eye color"""
        return self._eyes

    @eyes.setter
    def eyes(self, color: str):
        """Set the king's eye color"""
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Eyes color must be a non-empty string")
        self._eyes = color

    @property
    def hairs(self):
        """Get the king's hair color"""
        return self._hairs

    @hairs.setter
    def hairs(self, color: str):
        """Set the king's hair color"""
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Hair color must be a non-empty string")
        self._hairs = color

    def die(self):
        """Kill the king"""
        super().die()
