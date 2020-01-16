import types


class CsvReader():
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_top
        self.filename = filename
        self.mode = 'r'
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        if self.iscorrupted():
            self.file.close()
            self.file = None
        return self.file

    def __exit__(self, type, value, traceback):
        if self.file is not None:
            self.file.close()

    def iscorrupted(self):
        self.file.data = ""
        first_line = self.file.readline()
        if self.header is True:
            self.file.header = first_line
        else:
            self.file.header = None
            self.file.data = first_line
        number = len(first_line.split(self.sep))
        for line in self.file:
            self.file.data += line
            list = line.split(self.sep)
            if number != len(list):
                return True
            for elmt in list:
                if elmt is "\n":
                    return True

        def getdata(self):
            return self.data
        self.file.getdata = types.MethodType(getdata, self.file)

        def getheader(self):
            return self.header
        self.file.getheader = types.MethodType(getheader, self.file)
        return False
