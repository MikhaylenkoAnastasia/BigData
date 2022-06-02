def backspace(string : str):
    s = ''
    for i in range(len(string)):
        if i == len(string)-1 and string[i] != '#':
            s = s + string[i]
            break
        elif string[i] != '#' and string[i+1] != '#':
            s = s + string[i]
    return s

def backspace_compare(first: str, second: str):
    if backspace(first) == backspace(second):
        return True
    else: return False

print(backspace_compare("ab#c","ad#c"))
print(backspace_compare("a##c","#a#c"))
print(backspace_compare("a#c","b"))