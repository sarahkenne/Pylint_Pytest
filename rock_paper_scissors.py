"""
This module contains functions to perform random operations respectively,
manage time and interact with the operating system.
"""
import os
import random
import time


class RockPaperScissors:
    """This class represents the game Rock Paper Scissors.

     Attributes:
         our_choices (list): A list of possible choices in the game.
         green (str): green color used for display.
         scores (dict): A dictionary containing player scores.
    """

    def __init__(self):
        """Initializes the rock paper scissors game."""
        self.our_choices = ["rock", "paper", "scissors"]
        self.green = "\033[0;32m"  # Sets green color for display
        self.scores = {"player": 0, "computer": 0}

    def valid_answer(self, answer):
        """
        Checks if the answer is valid.

        Args:
            answer (str): The answer to check.
        Returns:
            string: The player's choice.
        """
        return answer in self.our_choices

    def winning_answer(self, answer1, answer2):
        """Determines if the first answer wins over the second."""
        return ((answer1 == "rock" and answer2 == "scissors") or
                (answer1 == "paper" and answer2 == "rock") or
                (answer1 == "scissors" and answer2 == "paper"))

    def equal_answer(self, answer1, answer2):
        """This function compares the two answers and clears the screen if they are the same.
        Args:
            answer1 (str): The first answer.
            answer2 (str): The second answer.
        Returns:
            bool: True if the answers are the same, False otherwise.
        """
        if answer1 == answer2:
            os.system("cls" if os.name == "nt" else "clear")  # Clears the screen
            return True
        return False

    def get_player_choice(self):
        """Asks the player to enter their choice.
        Returns: string: The player choice.
        """
        while True:
            player_answer = input("Type your choice: ").lower()
            if self.valid_answer(player_answer):
                return player_answer
            print("Not a valid option, expecting:", ", ".join(self.our_choices))

    def play_round(self, player_answer):
        """plays a round of the game"""
        # Random choice of computer among the available options
        pc_answer = random.choice(self.our_choices)

        print("You choose:", player_answer)
        time.sleep(0.5)
        print("Computer is thinking...")
        time.sleep(1)  # Pause to simulate computer thinking
        print("Computer choose:", pc_answer)
        print('\n')

        if self.equal_answer(player_answer, pc_answer):
            print("IT'S A TIE!!!")
        elif self.winning_answer(player_answer, pc_answer):
            print(player_answer, "beats", pc_answer)
            print("YOU WIN!!!")
            self.scores["player"] += 1  # Increments player score
        else:
            print(pc_answer, "beats", player_answer)
            print("YOU LOSE!")
            self.scores["computer"] += 1  # Increments computer score

    def display_scores(self):
        """Displays the current player and computer scores."""
        print("Player Score:", self.scores["player"])  # Displays player score
        print("Computer Score:", self.scores["computer"])  # Displays computer score

    def play_game(self):
        """Main function to play the Rock Paper Scissors game."""
        running = True
        print(self.green)
        print("### Rock Paper Scissors Game ###")

        while running:
            player_answer = self.get_player_choice()
            self.play_round(player_answer)
            self.display_scores()  # Displays current scores

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break

        print("Have a good day")  # Displays end of game message


if __name__ == "__main__":
    game = RockPaperScissors()  # Initializes the game
    game.play_game()
