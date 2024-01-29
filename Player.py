class Player:
    def __init__(self, name:str):
        self.wins = 0
        self.name = name
        self.message = ""
        self.indexList = [-1, -1]
        self.pairs = 0
    
    def Winner(self) -> None:
        self.wins += 1
    
    def Reset(self) -> None:
        self.pairs = 0
        self.indexList = [-1, -1]
        
    def NewPair(self) -> None:
        self.pairs += 1

    def SetMessage(self, message:str) -> None:
        self.message = message

    #* Give feedback if it is neccessary to the player and waits for its move
    def Play(self) -> str:
        print(self.message)
        throw = input(self.name + ": ")
        return throw