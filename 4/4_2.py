import sys

s = sys.argv
s.pop(0)
s.reverse()
s1 = ''
for i in s:
    s1 += i
    s1 += ' '
print s1[:len(s1) - 1]
