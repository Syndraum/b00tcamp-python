import sys
import string


def main(argv):
    if len(argv) < 3:
        print("ERROR")
        sys.exit(0)
    str = argv[1]
    len_min = 0
    try:
        len_min = int(argv[2])
    except ValueError:
        print("ERROR")
        sys.exit(0)
    line = str.translate({ord(c): None for c in string.punctuation}).split()
    tab = [word for word in line if len(word) > len_min]
    print(tab)


if __name__ == "__main__":
    main(sys.argv)
