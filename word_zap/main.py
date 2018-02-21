import player, random
def getUserint(prompt):
    while True:
        userinput = input(prompt)
        try:
            if int(userinput) > 0:
                return int(userinput)
        except:
            print("You can't convert that string to a int. Try again. ")

def getUserString(prompt):
    while True:
        userinput = input(prompt)
        userinput = userinput.strip()
        if userinput != '':
            return userinput.strip()

def getPlayers():
    playerlist = []
    players = getUserint('How many players will there be? ')
    for i in range(1,players+1):
        p=player.Player(getUserString('Name of player ' + str(i) + ' '))
        playerlist.append(p)
    return playerlist

def converToLower(prompt):
    return getUserString(prompt).lower()





def main():
    print("""Welcome! Time to play! Try to use all of your letters.
The first player that uses all of their letters wins!""")
    print('Great, Lets play!')
    players = getPlayers()


    while True:
        for player in players:

            current_letters = player.printLetters()
            if len(player.getLetters()) == 0:
                print(player.getName() + ' Won!')
                exit()
            print(player.getName() + ' it is your turn')
            print('Your current letters are ' + current_letters)

            while True:
                word = input('Enter a word. ')
                if word == '':
                    player.drawLetter()
                    break
                elif player.checkWord(word):
                    break







if __name__ == '__main__':
    main()
