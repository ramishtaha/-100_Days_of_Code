def hcf(a, b):
    hcf = 1
    h = 0
    while(hcf < a or hcf < b):
        if(a % hcf == 0 and b % hcf == 0):
            h = hcf
        hcf += 1
    return h



def main():
    n1 = int(input("Enter 1st Number:\n"))
    n2 = int(input("Enter 2nd Number:\n"))
    print(f"The Hcf of {n1} and {n2} is {hcf(n1, n2)}.")

main()