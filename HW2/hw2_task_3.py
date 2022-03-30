from typing import Any


def custom_range(mas: str, *args: Any):
    if len(args) == 1:
        index = mas.index(args[0])
        return mas[:index]
    elif len(args) == 2:
        start_index = mas.index(args[0])
        end_index = mas.index(args[1])
        return mas[start_index:end_index]
    elif len(args) > 2:
        start_index = mas.index(args[0])
        end_index = mas.index(args[1])
        return mas[start_index:end_index:args[2]]
    else:
        return mas



