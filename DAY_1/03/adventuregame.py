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



def printpause(s):
    time.sleep(random.randint(1,2))
    print(s)

main()