import sys


def main(argv):
    if len(argv) == 2:
        x = 0
        try:
            x = int(argv[1])
        except ValueError:
            print("ERROR")
            return 0
        if x == 0:
            print("I'm Zero.")
        elif x % 2 == 1:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    elif len(argv) > 2:
        print("ERROR")


if __name__ == "__main__":
    main(sys.argv)
