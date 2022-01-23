import random


class Card:

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        self.score = 300

    def draw(self):
        """Generates a new random value for the Card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 15)
