import sys

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
k = 0
c = 0
b = 0
if a1 >= 0 and a2 <=999999:
    for i in range(a1, a2 + 1):
        s = str(i)
        if len(s) < 6:
            s = s.rjust(6, '0')
        c = int(s[0]) + int(s[1]) + int(s[2])
        b = int(s[3]) + int(s[4]) + int(s[5])
        
        if c == b:
            k += 1

print k
