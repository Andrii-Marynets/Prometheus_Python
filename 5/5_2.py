import sys
a = sys.argv[1]
b = sys.argv[2]
def counter(x, y):
    t1 = str(x)
    t2 = str(y)
    count = 0
    for i in t1:
        for j in t2:
            if i == j:
                count +=1
                t1 = t1.replace(i, '')
                t2 = t2.replace(j, '')
                break
    return count
print counter(a, b)
