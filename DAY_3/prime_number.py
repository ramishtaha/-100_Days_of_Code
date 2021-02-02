def main():
    num = int(input("Enter a number to check:\n"))
    if(is_prime(num)):
        print("Number", num, "is Prime")
    else:
        print("Number", num, "is not Prime")
def is_prime(a):
    p = True
    for i in range(2, a):
        if(a % i == 0):
            p = False
            break
    return p

main()
