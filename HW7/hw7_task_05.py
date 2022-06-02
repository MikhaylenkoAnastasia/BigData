from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    >>> b = merge_sorted_files(["src/task_05_1.txt", "src/task_05_2.txt"])
    >>> list(b)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> type(b)
    <class 'list_iterator'>

    :param file_list:
    :return:
    """
    mas = []
    for i in file_list:
        with open(i) as file:
            for line in file:
                mas.append(int(line))
    return iter(sorted(mas))

b = merge_sorted_files(["src/task_05_1.txt", "src/task_05_2.txt"])
print(list(b))
print(type(b))
