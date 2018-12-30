b = (1,2,3,4,5,6,7,8,9)
print(b[-1:]+b[:-1])

def rotate(a, n):
    return a[-n:] + a[:-n]
                # concept of 2 rotation in
c = rotate(b,1)
print(c)

print (c[-1:]+ c[:-1])

