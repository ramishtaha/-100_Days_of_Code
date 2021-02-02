def is_even(num):
    if (num % 2 is 0):
        return True
    else:
        return False

def main():
    for i in range(1,20):
        if is_even(i):
            print((i * 2), "\n")
        else:
            print((i * 3), "\n")

        
main()