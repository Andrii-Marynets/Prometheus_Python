import sys

s = "mystring1Gni rts ym"
s1 = s.split(' ')
s = ''
for i in s1:
    s += i.lower()
s.lower()
s1 = ''

s1 = s[::-1]

if s == s1:
    print "YES"
else:
    print "NO"


    
