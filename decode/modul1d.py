import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

d = {i: key[alphabet.find(i):alphabet.find(i) + 5] for i in alphabet}

inText = sys.argv[1]
inText = inText.replace(' ', '')
t = ''
for i in range(0, len(inText), 5):
    t += inText[i:i+5] + ' '
t = t.rstrip()
t = t[:t.rfind(' ')]
t2 = ''
for i in t:
    if i.islower():
        t2 += 'a'
    elif i.isupper():
        t2 += 'b'
    else:
        t2 += ' '
t2 = t2.split(' ')
res = ''   
for i in t2:
    for j in alphabet:
        if i == d.get(j):
            res += j
print res


