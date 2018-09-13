
l=[1,2,4,3,2,5,7,4,2,7,4,3,6]
i={}
for x in l:
    if x in i.keys():
        i[x]+= 1
    else:
        i[x]=1
        print("Numbers ➢➢➢ count")
for x in i:
    print("    {}   ➢➢➢  {}".format(x,i[x]))
