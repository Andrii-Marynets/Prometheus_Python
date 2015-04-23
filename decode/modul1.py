key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

d = {i: key[alphabet.find(i):alphabet.find(i) + 5] for i in alphabet}

p = "Prometheus"
k = ''
p = p.lower()

for i in p:
    k += d[i] + ' '
k = k.strip()
print k

text = "Welcome to the Hotel California Such a lovely place Such a lovely place"

text = text.lower()

#dod 1
c = [i for i in range(0, len(text)) if text[i] == ' ']

text = text.upper()
text = text.replace(' ', '')

print text
t2 = ''
for i in range(0, len(k)):
    if k[i] == 'a':
        t2 += chr(ord(text[i]) + 32)
    else:
        t2 += text[i]
print t2
t2 += text[len(t2):]
print t2
