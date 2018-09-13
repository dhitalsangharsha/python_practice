age=int(input("what is your age?"))
print("you will die in " + str(90-age)+ " years")
print("you will die in {} years".format(90-age))
print("you will die in %d years" %(90-age))

l=[89,77,88,57,87,21,35,36]
l2=[]
for i in l:
    if i>=80:
        l2.append(i)
print(l2)


l2=[i for i in l if i>=80]
print(l2)