import random

class Board:
    def __init__(self):
        self.Board = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I']
        self.EmptyBoard  = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.guide = "\tGUIDE\n0  1  2  3  4  5\n6  7  8  9  10 11\n12 13 14 15 16 17\n"

    def Reset(self) -> None:
        random.shuffle(self.Board)
        for i in range(len(self.EmptyBoard)):
            self.EmptyBoard[i] = ' '

    #* Check if the index exists in the board and if it is empty
    def Check(self, index:str) -> str:
        try:
            indexI = int(index)
            if self.EmptyBoard[indexI] == ' ':
                return "DONE"
            return "INVALID MOVE"
        except Exception:
            return "INVALID MOVE"

    #* Show an especific card
    def ShowMove(self, index: int) -> None:
        self.EmptyBoard[index] = self.Board[index]
    
    def MatchMove(self, index:[int, int]) -> bool:
        if self.EmptyBoard[index[0]] == self.EmptyBoard[index[1]]:
            return True
        return False

    #* Hide cards
    def HideMove(self, index:[int, int]) -> None:
        self.EmptyBoard[index[0]] = ' '
        self.EmptyBoard[index[1]] = ' '

    def IsGameOver(self) -> bool:
        if ' ' not in self.EmptyBoard:
            return True
        return False

    def PrintBoard(self) -> None:
        print(self.guide)
        print(self.EmptyBoard[0] + '|' + self.EmptyBoard[1] + '|' + self.EmptyBoard[2] + '|' + self.EmptyBoard[3] + '|' + self.EmptyBoard[4] + '|' + self.EmptyBoard[5])
        print('-+-+-+-+-+-')
        print(self.EmptyBoard[6] + '|' + self.EmptyBoard[7] + '|' + self.EmptyBoard[8] + '|' + self.EmptyBoard[9] + '|' + self.EmptyBoard[10] + '|' + self.EmptyBoard[11])
        print('-+-+-+-+-+-')
        print(self.EmptyBoard[12] + '|' + self.EmptyBoard[13] + '|' + self.EmptyBoard[14] + '|' + self.EmptyBoard[15] + '|' + self.EmptyBoard[16] + '|' + self.EmptyBoard[17])