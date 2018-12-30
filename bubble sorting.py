x = [10,7,8,5,45,4,5,8,6,2,5,5,2,5,8,6,2]



for i in range(len(x)-1,0,-1):
    for k in range(i):
        if x[k] <= x[k + 1]:
            continue
        else:
            x[k] = x[k] + x[k + 1]
            x[k + 1] = x[k] - x[k + 1]
            x[k] = x[k] - x[k + 1]
    print(x)

print(x)




