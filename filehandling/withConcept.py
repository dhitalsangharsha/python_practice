with open("test.txt",'w') as fp:
    fp.write("test\n")
    fp.write("test2\n")

l=list(range(0,10))

with open("test1.txt",'w')as fp:
    for each in l:
        fp.write(str(each)+"\n")