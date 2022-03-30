from typing import List, Any
import itertools


def combinations(*args: List[Any]) -> List[list]:
    a = []
    for i in itertools.product(*args):
        a.append(i)
    return a


