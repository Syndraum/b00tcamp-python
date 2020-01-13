import sys
from count import text_analyzer


def main():
    if len(sys.argv) > 1:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()


if __name__ == "__main__":
    main()
