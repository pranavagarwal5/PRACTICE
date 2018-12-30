# SELECTION SORT CODE


def sel_sort(x):
    min = 0

    for i in range(len(x)-1):
        for j in range(i,len(x)-1):
            if x[i] > x[j + 1]:
                min = x[j + 1]
                x[j+1] = x[i]
                x[i]   = min
            else:
                min = x[i]
        print(x)

y = [10,7,8,5,45,4,5,8,6,2,5,5,2,5,8,6,2.45]
sel_sort(y)

print(y)


