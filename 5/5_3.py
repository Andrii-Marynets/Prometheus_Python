n = 8
m = 2

def super_fibonacci(n, m):
    if n < m:
        return 1
    arr = [1 for i in range(0, m)]
    for i in range(n - m):
        res = 0
        for j in arr:
            res += j
        arr.pop(0)
        arr.append(res)
    return res
print "Res:", super_fibonacci(n, m)
