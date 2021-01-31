import time
import random
def main():

    printpause('Hello, I am the Gatekeeper and I am here to warn you')
    printpause('WARING!! This Game is not for faint hearted')
    printpause('Do you wish to continue? (Type 1 for Yes or Type 0 to Exit)')
    choice = int(input())
    if(choice == 1):
        adventuregame()
    else:
        exit()

def adventuregame():
    printpause('Welcome to the game')
    printpause('You are in front of a House at midnight which is roumored to be haunted')
    printpause("It's raining heavily and it's very dark except some moments when lightning strikes")
    printpause("There's a small store room beside the House")
    printpause("You have 2 Options")
    printpause("Enter the Haunted House (Type 0) Enter the store room (Type 1)")
    choice = int(input())
    if(choice == 0):
        hauntedhouse(False)
    else:
        storeroom()

def storeroom():
    printpause('You enter the Storeroom')
    printpause('You found a Flashlight')
    printpause('Now, You are Entering Haunted House')
    hauntedhouse(True)

def hauntedhouse(flashlight):
    if(flashlight):
        printpause("You found that there's a tape recorder which was playing scary sounds")
        printpause("You understood that this was a prank and the house is not haunted")
        printpause("YOU WON")
        exit()
    else:
        printpause("You hear some scary sound and you are scared as shit")
        printpause("You ran away from the haunted house swearing to not come back again")
        printpause("You Lost")
        exit()



def printpause(s):
    time.sleep(random.randint(0,3))
    print(s)

main()