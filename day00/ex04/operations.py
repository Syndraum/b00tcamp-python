import sys
import argparse


def print_usage():
    print("Usage: python oprations.py")
    print("Exemple:")
    print("    python oparation.py 10 3")


def main(argv):
    argvlen = len(argv)
    if argvlen > 3:
        print("InputError: too many arguments\n")
    if argvlen != 3:
        print_usage()
        sys.exit(0)
    x = 0
    y = 0
    try:
        x = int(argv[1])
        y = int(argv[2])
    except ValueError:
        print("InputError: only numbers\n")
        print_usage()
        sys.exit(0)
    print("Sum:\t\t" + str(x + y))
    print("Difference:t\t" + str(x - y))
    print("Product:t\t" + str(x * y))
    print("Quotient:t\t", end='')
    if y == 0:
        print("ERROR (div by zero)")
    else:
        print(x / y)
    print("Remainder:t\t", end='')
    if y == 0:
        print("ERROR (modulo by zero)")
    else:
        print(x % y)


if __name__ == "__main__":
    main(sys.argv)
