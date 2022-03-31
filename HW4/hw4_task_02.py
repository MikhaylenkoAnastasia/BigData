import doctest

def read_magic_number(path: str) -> bool:
    """
    This function reads a file and check a values into the file.
    :param path: adress to file with data.
    :return: True if 1<= values < 3 in file, else False or ValueError if values in file is not a number

    >>> read_magic_number("src/file_true.txt")
    True
    >>> read_magic_number("src/file_false.txt")
    False
    >>> read_magic_number("src/file_error.txt")
    <class 'ValueError'>
    """
    with open(path) as file:
        result = True
        try:
            linenumber = file.readline().split()
            for i in range(0, len(linenumber)):
                if float(linenumber[i]) >= 1.0 and float(linenumber[i]) < 3.0:
                    pass
                else:
                    return False
        except ValueError:
            return ValueError

        return result

if __name__ == '__main__':
    doctest.testmod()

# print(read_magic_number("src/file_true.txt"))
