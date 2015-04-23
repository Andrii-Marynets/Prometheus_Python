import math
def convert_n_to_m(x, n, m):
    if x == 0:
        return 0
    if m == 1:
        return '0'
    if isinstance(x, list) or isinstance(x, float):
        return False
    if isinstance(x, long):
        x = int(x)
    x = str(x)
    b = x.count('0')
    if b == len(x):
        return 0
    x = x.upper()
    d = {}
    c = ord('A')
    for i in range(10, 36):
        d[str(i)] = chr(c)
        c += 1
    s = ''
    for i in x:
        s += i + ' '
    s = s.split()
    for i in range(0, len(s)):
        for j in d:
            if s[i] == d[j]:
                s[i] = j
                break
    l = []
    for i in range(0, len(s)):
        l.append(n ** i)
    l.reverse()
    dec = 0
    for i in range(0, len(s)):
        dec += int(s[i]) * l[i]
    res = []
    while(dec > 0):
        res.append(str(dec % m))
        dec = dec / m
    res.reverse()
    for i in range(0, len(res)):
        if res[i] < '9':
            for j in range(10, 36):
                if res[i] == str(j):
                    res[i] = d[str(j)]
    res = str(res)
    res = res.replace(',', '')
    res = res.replace('[', '')
    res = res.replace(']', '')
    res = res.replace(' ', '')
    res = res.replace('\'', '')
    return res
print convert_n_to_m("ZZZZ", 35, 13)
