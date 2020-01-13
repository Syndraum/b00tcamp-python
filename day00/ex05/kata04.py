def main():
    value = (0, 4, 132.42222, 10000, 12345.67)
    print(
        "day_" + "%02d" % value[0] + ',',
        "ex_" "%02d" % value[1], ':',
        "%.2f" % value[2] + ',',
        "%.2e" % value[3] + ',',
        "%.2e" % value[4])


if __name__ == "__main__":
    main()
