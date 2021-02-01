def listcomp(st):
    ls = [letter for letter in st]
    return ls


def main():
    st = input("Enter a String to make a list: \n")
    ls = listcomp(st)
    print(ls)

main()