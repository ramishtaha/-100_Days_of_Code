def main():
    num = int(input("Enter a Number:\n"))
    print("Factorial of ", num, " is:\n", factorial(num))

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

main()