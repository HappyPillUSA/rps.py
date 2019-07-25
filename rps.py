# Optional Project "Rock Paper and Scissors"
# Anny L Grijalba
# A path to learn en terms  of OOP.
# Define classes, create objects and how to interact with them.

import random
import time


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round. after the user plays 
rounds ,program will ask him/her to try a Match, program will 
display the final winner, and ask to play again..."""

moves = ['rock', 'paper', 'scissors']
"""List for player moves"""


def print_pause(message):
    """A Function to display message with delay """
    print(message)
    time.sleep(1)


def display_intro():
    """A "Little introduction to this version of Rock, scissors and paper"""
    print("\n" * 5)
    print_pause("Rock, Paper, Scissors was actually created in China.\n")
    print_pause("The rest, as they say, is history.\n")
    print_pause("*   " * 5)
    print()
    print_pause("In this version, user wil learn how to play by ,\n")
    print_pause("by choosing the number of rounds,\n")
    print_pause("then his/her can play a match of 3 rounds against\n")
    print_pause("the chosen Virtual Player. Finally it will announced:\n")
    print_pause("who will be the W I N N E R !\n")
    print()
    print_pause("*   " * 5)


class Player:
    """The Player class is the parent class for all of the Players
    in this game - class attributes and methods-
    score class instance var"""

    my_move = None
    their_move = None
    score = 0

    def move(self):
        pass


    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


class Rocker(Player):
    """Method : This player always plays 'Rock?."""

    def move(self):
        return 'rock'


class RandomPlayer(Player):
    """subclass-Player that chooses its moves at random.- random module"""

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    """Subclass- Allows the user to choose  his/her moves.
    Task: validate Human Player moves input.
    Adding a personal touch, to differentiated
    from the virtual Player"""

    def __init__(self):
        self.name = input("Please, type your name to star The Game\n")
        self.score = 0

    def move(self):
        move = input("Rock, Paper or Scissors?\n")
        while move.lower().strip() not in moves:
            print("I didn't understand your choice. Please try again")
            move = input("Please enter rock, paper, or scissors.\n")

        return move


class ReflectPlayer(Player):
    """Subclass that "remember"what move the Opponent player.
       This player will 'learn' the other players move (their-move)"""

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        """This method 'teach' the player his opponents move."""
        self.their_move = their_move
        self.my_move = my_move


class CyclePlayer(Player):
    """Subclass that cycle to different players' move."""
        # My next task will be change move method
        #into dictionay"""

    def move(self):

        if self.my_move is None:
            return random.choice(moves)
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


def beats(one, two):
    """Game rules - return"""
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    """Class game , player choose number of rounds.
    counts moves announces winner"""
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.name = self.p1.name
        self.p2.name = "Virtual PLayer"

    def play_round(self):
        """ Method to play round according to beat function"""
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"{self.p1.name} : {move1} - {self.p2.name} : {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            print(f"{self.p1.name} beats {self.p2.name}")
            self.p1.score += 1
        elif beats(move2, move1) is True:
            print(f"{self.p2.name} beats {self.p1.name}")
            self.p2.score += 1
        elif move1 == move2:
            print("It was a Tie!\n")
        print(f"{self.p1.name}: {self.p1.score} points\n")
        print(f"{self.p2.name}: {self.p2.score} points\n")
        print()
        print("=" * 38)

    def play_game(self):
        print_pause("Game start!")
        print(f" PLAYER 1 :{ self.p1.name}  VS PLAYER 2 :{ self.p2.name} \n")
        print("     Rock,Scissor & Paper Game ")
        print("=" * 38)
        while True:
            game_number = ""
            try:
                game_number = int(input("How many rounds,\n"
                                        "would you like to play?\n"))
            except ValueError:
                print("Sorry, I didn't understand that.\n")
                continue
            if game_number <= 0:
                print("Sorry, your response must not be 0 or negative")
                continue
            else:
                break
        print(f"Game start! You have {game_number} rounds, let's go!")
        for n in range(int(game_number)):
            print()
            print(f"Round {n + 1}:")
            print("=" * 8)
            Game.play_round(self)
        print_pause("Excellent! Now, that you know how to play Rounds...\n")
        Game.play_set(self)

    def game_match(self):
        # next task will be to color the results
        print_pause(f"Player 1: {self.p1.name} VS. Player 2: {self.p2.name}\n")
        print_pause("Match  start!")
        for rounds in range(3):
            print(f"Round {rounds +1}:")
            self.play_round()
        # next task: a method to compare results of each player
        # and declare the Winner
        if self.p1.score == self.p2.score:
            print("No winner!\n")
        elif self.p1.score > self.p2.score:
            print(f"{self.p1.name} is the WINNER "
                  f"by {self.p1.score - self.p2.score} points\n")
        elif self.p2.score > self.p1.score:
            print(f"{self.p2.name} is the WINNER "
                  f"by {self.p2.score - self.p1.score} points\n")
        print_pause("MATCH OVER")
        print_pause("*   " * 5)
        self.play_again()
        self.play_game()

    def play_set(self):
        """Ask the user to play a set of 3 rounds"""
        match = input("Would you like to play a match? -set of 3 Rounds\n"
                      "Enter 'Y' for 'Yes' or\n"
                      "Enter 'N' for 'NO'\n").lower()
        if "y" in match:
            print_pause(f"Good choice. Starting game up.")
            self.game_match()
        elif "n" in match:
            print_pause(f"Thanks for playing! Good bye!")
            exit()
        else:
            print_pause(f"Please enter a valid answer '(Y/N)'.")
            return self.play_set()

    def play_again(self):
        """This method take the user input to
        play again or to exit the game."""
        playing_again = input("Would you like to play again?"
                              "(Type: Yes or NO) \n").lower()
        if 'yes' in playing_again:
            return
        elif 'no' in playing_again:
            print_pause("Thanks for playing, Bye.")
            return exit()
        else:
            print_pause("Enter a valid answer, type 'YES or 'NO'")
        self.play_again()


if __name__ == '__main__':
    """Footer condition to run the code directly """

    display_intro()
    style = {"1": Rocker(), "2": RandomPlayer(),
             "3": CyclePlayer(), "4": ReflectPlayer()}
    """  keys will be  the user choice for Virtual Player style
         and the  values will be objects'"""

    user_choice = ""
    while user_choice not in style:
        user_choice = input("Lets begin selecting your Virtual Player: \n "
                            "Enter: 1, 2, 3, or 4 \n"
                            "1.Rocker  ---->  Always plays the same move,  \n"
                            "2.Randy   ---->  Plays  at random\n"
                            "3.Reflecy ---->  Remembers your last move\n"
                            "4.Cycle   ---->  Cycles the three styles\n")

    game = Game(HumanPlayer(), style[user_choice])
    game.play_game()
