import os


def main():
    stillPlaying = True
    while (stillPlaying):
        answer = raw_input("Start a new game? (y/n): ")
        if answer == 'y' or answer == 'Y':
            startGame()
        elif answer == 'n' or answer == 'N':
            stillPlaying = False
        else:
            print("Please type 'y' or 'n'.")

    print("Later!")


def evaluateHand(cards):
    return sum(cards)


def startGame():
    print
    gameOver = "Game Over."
    name = raw_input("What... is your name?\n> ")
    if name.lower() != os.getenv("USER"):
        print
        raw_input(gameOver)
        print
        return

    print
    quest = raw_input("What... is your quest?\n> ")
    if quest == '':
        print
        raw_input(gameOver)
        print
        return

    print
    question = "What... is the airspeed velocity of an unladen swallow?\n> "
    airspeed = raw_input(question)
    if airspeed.lower() != 'an african or european swallow?':
        print
        raw_input(gameOver)
        print
        return

    print
    raw_input("What? I... I don't know that...")
    print
    raw_input("Arrrrrrrrrggggggh")
    print
    raw_input("You win! How do you know so much about swallows?")
    print
    raw_input(gameOver)
    print

if __name__ == '__main__':
    main()
