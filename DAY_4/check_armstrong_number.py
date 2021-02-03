def main():
    num = int(input("Enter the Number to check for Armstrong Number"))
    if(is_armstrong(num)):
        print(f"The Number {num} is an Armstrong Number")
    else:
        print(f"The Number {num} is not an Armstrong Number")


def is_armstrong(a):
    temp = a
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp = temp // 10
    if (sum is a):
        return True

    else:
        return False


main()
        
