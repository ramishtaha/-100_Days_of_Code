def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if(greater % a == 0 and greater % b == 0):
            return greater
        greater += 1



def main():
    n1 = int(input("Enter 1st Number:\n"))
    n2 = int(input("Enter 2nd Number:\n"))
    print(f"The Lcm of {n1} and {n2} is {lcm(n1, n2)}.")

main()