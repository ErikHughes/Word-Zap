import random

class Player:
    def __init__(self, name):
        self.name = name
        self.letters = []
        for i in range(7):
            self.drawLetter()

    def getName(self):
        return self.name

    def getLetters(self):
        return self.letters

    def drawLetter(self):
        letter = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        l = random.choice(letter)
        self.letters.append(l)
        return l

    def printLetters(self):
        letters = self.getLetters()
        playerletters = ''
        for letter in letters:
            playerletters += letter + ' '
        return playerletters.strip()

    def checkWord(self,word):
        copy = self.getLetters()[:]
        for l in word:
            if l in copy:
                copy.remove(l)
            else:
                return False
        self.letters = copy
        return True
