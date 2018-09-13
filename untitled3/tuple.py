t=(1,2,3)
print(t,type(t))
print(t[0])

def swap(i,j):
    return(j,i)
a=5
b=6
print(a,b)
a,b =swap(a,b)
print(a,b)

l=[(1,2),(3,4)]
for x in l:
    for i in x:
        print(i)

    for x in l:
        print("x:{},y:{}".format(x[0],x[1]))

        t=(1,2,3,4,5)
        for i in t:
            print(i)