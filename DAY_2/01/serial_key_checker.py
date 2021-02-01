#a serial key checker for windows 95

def serialcheck(serial):
    part1 = int(serial[0:3])
    if(part1 == 222 | part1 == 333 | part1 == 444 | part1 == 555 | part1 == 666 | part1 == 777 | part1 == 888 | part1 == 999):
        print("Wrong Serial Number.")
    else:
        if(checkmod7(serial)):
            print("Correct Serial Number.")
        else:
            print("Wrong Serial Number.")


# Checks if the sum of the digits is divisible by 7.
def checkmod7(serial):
    sum = 0
    for i in range(4, 11):
        sum += int(serial[i])
    if(sum % 7 == 0):
        return True
    else:
       return False


# Main Function to drive the program
def main():
    serial = input("Enter Serial Number.")
    serialcheck(serial)

main()