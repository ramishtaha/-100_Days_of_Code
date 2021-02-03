def main():
    year = int(input("Please Enter the Year:\n"))
    if(isleap(year)):
        print("The Year " + str(year) + " is a Leap Year")
    else:
        print("The Year " + str(year) + " is not a Leap Year")
def isleap(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

main()