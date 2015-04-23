n = "123"

def count_holes(n):
    d = ['0', '4', '6', '9']
    if n == None:
        return "ERROR"
    if isinstance(n, float) or isinstance(n, list) or isinstance(n, dict):
        return "ERROR"
    if isinstance(n, str):
        if '.' in n:
            return "ERROR"
        if n.isalpha() or n == '':
            return "ERROR"
        n = long(n)
    if isinstance(n, int):
        n = str(n)
    if isinstance(n, long):
        n = str(n)
    res = 0
    for i in n:
        if i in d:
            res += 1
        elif i == '8':
            res += 2
    return  res

print count_holes(n)