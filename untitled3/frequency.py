from collections import Counter
l=[1,2,4,3,2,5,7,4,2,7,4,3,6]
a= Counter(l)
for v in a:
    print("{} : {}".format(v,a[v]))
