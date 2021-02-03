def main():
    num = int(input("Enter the Natural Numbers:\n"))
    sum = 0
    for i in range(num + 1):
        sum += i
    print(f"{sum}")

main()