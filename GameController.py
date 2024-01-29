from Board import Board
from Player import Player
import os, sys, time

class GameController:
    def __init__(self):
        self.players = []
        self.board = Board()
        self.p1starts = 0

    def ShowInstructive(self) -> None:
        print("\t\t\tMEMORY GAME")
        print("INSTRUCTIVE")
        print("\n1: Each player has 2 moves per turn"
              "\n2: If your two throws match, it is still your turn"
              "\n3: In the end of the game, the player with the most pairs will win"
              "\n\nE: Exit")
    
    def SavePlayers(self) -> None:
        p1 = input("Name player 1: ")
        p2 = input("Name player 2: ")
        self.players.append(Player(p1))
        self.players.append(Player(p2))
    
    def Start(self) -> None:
        self.ShowInstructive()
        option = input(">")
        if option == "E":
            self.Exit()
        else:
            self.SavePlayers()
            self.board.Reset()
        self.UpdateBoard()
        # While game is running
        while True:
            # 2 moves per turn
            for i in range(2):
                # While a player is moving
                while True:
                    throw = self.players[self.p1starts].Play()
                    if throw == "E":
                        self.Exit()
                    # Move must be accepted
                    result = self.board.Check(throw)
                    if result == "DONE":
                        self.players[self.p1starts].SetMessage("")
                        # Save move and update the board
                        self.players[self.p1starts].indexList[i] = int(throw)
                        self.board.ShowMove(int(throw))
                        self.UpdateBoard()
                        break
                    # Give feedback to the player
                    self.players[self.p1starts].SetMessage(result)
            # Set pairs and check if it is game over
            if self.board.MatchMove(self.players[self.p1starts].indexList):
                self.players[self.p1starts].NewPair()
                self.UpdateBoard()
                if self.board.IsGameOver():
                    self.GameOver()
            # Hide cards and change player
            else:
                time.sleep(2)
                self.board.HideMove(self.players[self.p1starts].indexList)
                self.UpdateBoard()
                if self.p1starts == 1:
                    self.p1starts = 0
                else:
                    self.p1starts = 1

    #* Reset board, pairs of each player and wins
    def GameOver(self) -> None:
        print("\nGAME OVER")
        if self.players[0].pairs > self.players[1].pairs:
            print("\n" + self.players[0].name + " WINS")
            self.players[0].Winner()
        elif self.players[0].pairs < self.players[1].pairs:
            print("\n" + self.players[1].name + " WINS")
            self.players[1].Winner()
        for player in self.players:
            player.Reset()
        time.sleep(5)
        self.board.Reset()
        self.UpdateBoard()

    def Exit(self) -> None:
        sys.exit()

    #* Clear the screen and show the updated board
    def UpdateBoard(self) -> None:
        os.system('clear')
        for player in self.players:
            print(player.name + " WINS: " + str(player.wins) + " PAIRS: " + str(player.pairs))
        print("E: Exit")
        self.board.PrintBoard()