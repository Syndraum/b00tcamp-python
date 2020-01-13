def main():
    time = (3, 30, 2019, 9, 25)
    print(
        "%02d" % time[3] + '/'
        + "%02d" % time[4] + '/'
        + "%04d" % time[2] + ' '
        + "%02d" % time[0] + ':'
        + "%02d" % time[1])


if __name__ == "__main__":
    main()
