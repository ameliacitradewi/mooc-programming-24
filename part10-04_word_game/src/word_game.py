# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            pass

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)       

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiouAEIOU"
        vowels1_count = sum(1 for char in player1_word if char in vowels)
        vowels2_count = sum(1 for char in player2_word if char in vowels)

        if vowels1_count > vowels2_count:
            return 1
        elif vowels1_count < vowels2_count:
            return 2
        else:
            pass

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        valid_moves = {"rock", "paper", "scissors"}
        player1 = player1_word.lower()
        player2 = player2_word.lower()

        if player1 not in valid_moves and player2 not in valid_moves:
            return 0
        elif player2 not in valid_moves:
            return 1
        elif player1 not in valid_moves:
            return 2
        
        if player1 == player2:
            return 0
        elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
            return 1
        else:
            return 2