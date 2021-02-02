def main():
    num = int(input("Enter a length of fibonacci series:\n"))
    fibonacci(num)

def fibonacci(a):
    n1 = 0
    n2 = 1
    count = 2
    print(str(n1) + "\n" + str(n2))
    while (count < a):
        t = n1 + n2
        print(t)
        n1 = n2
        n2 = t
        count += 1

main()