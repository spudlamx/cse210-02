from hilo import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards_value = []
        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 300

        for i in range(2):
            card = Card()
            self.cards.append(card)


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        if self.total_score <= 0:
            self.is_playing = False
        else:
            draw_again = input("Draw again? [y/n] ")
            self.is_playing = (draw_again == "y")

        
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        
        for i in range(len(self.cards)):
            card = self.cards[i]
            card.draw()
            value = card.value
            self.cards_value.append(int(value))
        print(f'first card is {self.cards_value[-2]}')
        guess = input('Higher or lower? (h/l): ')
        card_1 = self.cards_value[-2]
        card_2 = self.cards_value[-1]
        if (card_1) >= (card_2) and guess == 'l' or (card_1) < (card_2) and guess == 'h':
            self.score = 100
        else:
            self.score = -75
        
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            print(f'Your final score is: {self.total_score}')
            return
        
        values = ""
        for i in range(len(self.cards)):
            card = self.cards[i]
            values += f"{card.value} "


        print(f'Next card is {self.cards_value[-1]}')
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)

