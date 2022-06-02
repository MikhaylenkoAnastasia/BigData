class KeyValueStorage():
    """
    >>> storage = KeyValueStorage('src/task_04.txt')
    >>> print(storage['name'])  # will be string 'kek'
    kek
    >>> print(storage.song)  # will be 'shadilay'
    shadilay
    >>> print(storage.power)  # will be integer 9001
    9001
    """
    my_dict = {}

    def __init__(self, path):
        self.path = path
        self.read_a_file()

    def read_a_file(self):
        with open(self.path) as file:
            while True:
                line = file.readline().split('=')
                if line == ['']:
                    break
                if not hasattr(self, line[0]):
                    setattr(self, line[0], line[1][0:len(line[1]) - 1])
                    self.my_dict[line[0]] = line[1][0:len(line[1]) - 1]

    def __getitem__(self, key):
        return self.my_dict[key]


storage = KeyValueStorage('task_04.txt')
print(storage['name'])  # will be string 'kek'
print(storage.song)  # will be 'shadilay'
print(storage.power)  # will be integer 9001
