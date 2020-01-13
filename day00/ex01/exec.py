import sys


def main():
    if len(sys.argv) > 1:
        print(" ".join(sys.argv[1:]).swapcase()[::-1])

if __name__ == "__main__":
    main()
