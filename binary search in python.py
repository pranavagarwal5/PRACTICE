from math import *
k= -1

def search(b, n):
    l = 0
    u = len(b)-1

    while l <= u:
        m = (l + u) // 2
        if b[m] == n:
            globals()['k'] = m
            return True

        else:
            if b[m] < n:
                l = m+1
            else:
                u = m-1

    return False


n=12
x = [1,7,3,4,5,6,7,4,9,10,11,12]
y = sorted(x)
print(y)

if search(y,n):
    print("found at", k)
else:
    print("not found")