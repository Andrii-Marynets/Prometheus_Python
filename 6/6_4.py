s = "Load up on guns; bring your friends It's fun to lose and to pretend She's over-bored and self-assured Oh no, I know a dirty word Hello,hello,hello,how low Hello,hello,hello,howlow Hello,hello,hello,how low Hello,hello,hello"

def find_most_frequent(text):
    text = str(text)
    if text == '':
        return []
    text = text.lower()
    text = text.replace('-', ' ')
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    text = text.replace(':', ' ')
    text = text.replace(';', ' ')
    text = text.replace('!', ' ')
    text = text.replace('?', ' ')
    res = text.split()
    d = {}
    for i in res:
        d[i] = res.count(i)
    r = []
    for i in d:
        r.append(d.get(i))
    mx = max(r)
    res = []
    for i in d:
        if d.get(i) == mx:
            res.append(i)
    return res

print find_most_frequent(s)