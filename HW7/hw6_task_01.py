from typing import Any


# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}

count = 0
def find_occurrences(tree: dict, element: Any) -> int:
    global count
    for value in tree.values():
        if isinstance(value,dict):
            find_occurrences(value,element)

        elif isinstance(value,list):
            for e in value:
                if isinstance(e,dict):
                    find_occurrences(e,element)
                else:
                    if e == element:
                        count = count + 1
        else:
            if value == element:
                count = count + 1
    return count

if name == 'main':
    print(find_occurrences(example_tree, "RED"))  # 6

