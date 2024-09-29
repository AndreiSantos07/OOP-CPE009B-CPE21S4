from Novice import Novice
from Swordman import Swordman
from Archer import Archer
from Magician import Magician
from Boss import Boss
import random


class Game:
    def __init__(self):
        self.wins_single_player = 0
        self.wins_player_vs_player = 0

    def select(self):
        while True:  # 1 and 2 only accepts to go next
            mode = input("\n(1) for Single Player \n(2) for Player vs Player \nSelect mode: ")
            if mode == "1":
                self.single_player()
                break  # After playing, it will exit since it is only single player mode
            elif mode == "2":
                self.player_vs_player()
                break  # It will break if there is already a winner
            else:
                print("Incorrect mode, please try again.") # If error mode was enetered, this line will be printed

    def single_player(self): #For single player mode
        player = Novice("Player")
        opponent = Boss("Monster")

        while True:
            self.play_match(player, opponent)

            if opponent.getHp() <= 0:
                print(f"{player.getUsername()} is the winner. Nice!")
                self.wins_single_player += 1
                if self.wins_single_player >= 2:
                    print("Congratulations, you leveled up! You can now choose different roles!")
                    player = self.select_role("Player")
                opponent = Boss("Monster")  # Reset opponent HP for the next match
            else:
                print(f"{opponent.getUsername()} wins. Try again, and keep it up!")
                break

    def player_vs_player(self): #For player vs player mode
        player1_name = input("Enter name for player 1: ")
        player2_name = input("Enter name for player 2: ")
        player1 = self.select_role(player1_name)
        player2 = self.select_role(player2_name)

        while True:
            self.play_match(player1, player2)
            if player1.getHp() <= 0:
                print(f"{player2.getUsername()} is the winner!")
                self.wins_player_vs_player += 1
                break
            elif player2.getHp() <= 0:
                print(f"{player1.getUsername()} is the winner!")
                self.wins_player_vs_player += 1
                break

    def select_role(self, name):
        print(f"{name}, select a role: \n1. Swordsman \n2. Archer \n3. Magician")
        role_choice = input("Enter your chosen role: ")

        if role_choice == "1":
            return Swordman(name)
        elif role_choice == "2":
            return Archer(name)
        elif role_choice == "3":
            return Magician(name)
        else:
            print("Invalid choice of role, your role : Novice.")
            return Novice(name)

    def play_match(self, player1, player2):
        players = [player1, player2]
        random.shuffle(players)
        current_player = players[0]
        opponent = players[1]

        while player1.getHp() > 0 and player2.getHp() > 0:
            damage = random.randint(5, 10)  # Random damage number between  and 10
            opponent.setHp(opponent.getHp() - damage)  # The updated health / hitpoints of the player
            print(f"{current_player.getUsername()} attacks {opponent.getUsername()} for {damage} damage!")
            print(f"{opponent.getUsername()} HP: {opponent.getHp()}")

            # Switch turns
            current_player, opponent = opponent, current_player

    def play(self):
        while True:
            self.select()

if __name__ == "__main__":
    game = Game()
    game.play()
