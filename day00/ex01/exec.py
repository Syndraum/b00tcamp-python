import sys


def	main():
	print(" ".join(sys.argv[1:]).swapcase()[::-1])
	
if __name__ == "__main__":
	main()