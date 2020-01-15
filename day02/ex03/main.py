from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        if file is None:
            print("File is corrupted")
        else:
            header = file.getheader()
            print("============ header ============\n", header)
            data = file.getdata()
            print("============ data ============\n", data)
