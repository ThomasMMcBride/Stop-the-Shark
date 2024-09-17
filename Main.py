import random

# Model: Saves current state of the hangman game
# Things worth saving:
    # Possible words in the game
    # Current word to guess
    # Letters guessed
    # Correct letter guesses
    # Incorrect letter guesses
# What should a model for the hangman game be able to do to itself?
    # Guess a letter
    # Provide information of its state
class Model:
    def __init__(self, possible_words):
        self.possible_words = possible_words
        self.word_to_guess = random.choice(self.possible_words)
        self.correct_letters = ["_"] * len(self.word_to_guess)
        self.incorrect_letters = []
        self.num_attempts = 10
    
    def guess_letter(self, letter):
        if letter.lower() in self.word_to_guess:
            for i, char in enumerate(self.word_to_guess):
                if letter == char:
                    self.correct_letters[i] = char
        else:
            self.incorrect_letters.append(letter.lower())
            self.num_attempts -= 1
    
    def game_over(self):
        return self.num_attempts == 0 and "_" in self.correct_letters
    
    def player_wins(self):
        return self.num_attempts > 0 and "_" not in self.correct_letters
    

# View: Displays information about the game to the player, and receives input from the player
# Things worth showing:
    # Current attempts left
    # Guessed word so far
    # Incorrect guesses
    # Let the player know if they have lost or won
    # Let them know if they've input something invalid
class View:
    @staticmethod
    def display_welcome():
        print("Welcome to Stop the Shark!\n")
    
    @staticmethod
    def display_game_over():
        print("Game over!\n")

    @staticmethod
    def display_game_won():
        print("YOU WIN!\n")
    
    @staticmethod
    def display_text(text):
        print(f"{text}\n")
    
    @staticmethod
    def get_next_guess():
        return input("\nWhat is your next letter guess?:")
    
    @staticmethod
    def display_try_again():
        print("Invalid input- please provide a letter")

    @staticmethod
    def print_space():
        print("\n\n\n\n")

    @staticmethod
    def show_man(stage):
        stages = [
        """
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ ||| / 
                      \|||/ 
                       \o/
                        |
                       / \\

             
            |-
            |  \\_
        ____|_____\\____________
        """,
        """
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ ||| / 
                      \| |/ 
                       \o/
                        |
                       / \\

                
            |-
            |  \\_
        ____|_____\\____________
        """,
        """
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ ||| / 
                       \|/ 
                       \o/
                        |
                       / \\

                     
            |-
            |  \\_
        ____|_____\\____________
        """,
        """
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ ||| / 
                       | |
                       \o/
                        |
                       / \\

                     
            |-
            |  \\_
        ____|_____\\____________
        """,
        """
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ | | / 
                       | |
                       \o/
                        |
                       / \\

                     
            |-
            |  \\_
        ____|_____\\____________
        """,
        """
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ | | / 
                        |
                       \o/
                        |
                       / \\

                      
            |-
            |  \\_
        ____|_____\\____________
        """,
        """
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ | | / 
                       \o/
                        |
                       / \\

                  
            |-
            |  \\_
        ____|_____\\____________
        """,
        """
                     _______
                   /         \\
                  |           |
                  |___________|
                      | | |    
                       \o/
                        |
                       / \\

            
            |-
            |  \\_
        ____|_____\\____________
        """,
        """
                     _______
                   /         \\
                  |           |
                  |___________|
                       | |     
                       \o/
                        |
                       / \\

              
            |-
            |  \\_
        ____|_____\\____________
        """,
        """
                     _______
                   /         \\
                  |           |
                  |___________|
                       |    
                       \o/
                        |
                       / \\

               
            |-
            |  \\_
        ____|_____\\____________
        """,
        """ 









           mmm food...       
            |-
            |  \\_      uh oh...
        ____|_____\\_____\o/____
        """,
        """
                      phew!
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ ||| / 
                      \|||/ 
                       \o/
                        |
                       / \\

        whatever...    
             -|
          _/  |
        /_____|__________________
        """,
        """
                      phew!
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ ||| / 
                      \| |/ 
                       \o/
                        |
                       / \\

        whatever...    
             -|
          _/  |
        /_____|__________________
        """,
        """
                      phew!
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ ||| / 
                       \|/ 
                       \o/
                        |
                       / \\

        whatever...    
             -|
          _/  |
        /_____|__________________
        """,
        """
                      phew!
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ ||| / 
                       | |
                       \o/
                        |
                       / \\

        whatever...    
             -|
          _/  |
        /_____|__________________
        """,
        """
                      phew!
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ | | / 
                       | |
                       \o/
                        |
                       / \\

        whatever...    
             -|
          _/  |
        /_____|__________________
        """,
        """
                      phew!
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ | | / 
                        |
                       \o/
                        |
                       / \\

        whatever...    
             -|
          _/  |
        /_____|__________________
        """,
        """
                      phew!
                     _______
                   /         \\
                  |           |
                  |___________|
                     \ | | / 
                       \o/
                        |
                       / \\

        whatever...    
             -|
          _/  |
        /_____|__________________
        """,
        """
                      phew!
                     _______
                   /         \\
                  |           |
                  |___________|
                      | | |    
                       \o/
                        |
                       / \\

        whatever...    
             -|
          _/  |
        /_____|__________________
        """,
        """
                      phew!
                     _______
                   /         \\
                  |           |
                  |___________|
                       | |     
                       \o/
                        |
                       / \\

        whatever...    
             -|
          _/  |
        /_____|__________________
        """,
        """
                      phew!
                     _______
                   /         \\
                  |           |
                  |___________|
                       |    
                       \o/
                        |
                       / \\

        whatever...    
             -|
          _/  |
        /_____|__________________
        """]

        print(stages[stage])


# Controller: Manipulate the view and controller and keep the game running until the game is over

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def go(self):
        self.view.display_welcome()

        while not self.model.game_over() and not self.model.player_wins():
            self.view.show_man(10 - self.model.num_attempts)
            self.view.display_text(f"Word guessed so far: {' '.join(self.model.correct_letters)}")
            self.view.display_text(f"Incorrect guesses: {', '.join(self.model.incorrect_letters)}")
            self.view.display_text(f"Number of guesses left: {self.model.num_attempts}")
            guess = self.view.get_next_guess()

            if len(guess) != 1 or not guess.isalpha():
                self.view.print_space()
                self.view.display_try_again()
                continue

            self.model.guess_letter(guess)
        
        if self.model.game_over():
            self.view.show_man(10)
            self.view.display_game_over()
        elif self.model.player_wins():
            self.view.show_man(21 - self.model.num_attempts)
            self.view.display_text(f"Number of attempts: {10 - self.model.num_attempts}")
            self.view.display_text(f"Final word: {''.join(self.model.correct_letters)}")
            self.view.display_game_won()


if __name__ == "__main__":
    words = ['colorstack', 'black', 'latinx', 'excellence', 'chipotle', "model", "view", "controller"]
    model = Model(words)
    view = View()
    controller = Controller(model, view)
    
    controller.go()

