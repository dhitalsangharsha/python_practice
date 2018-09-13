func = lambda x:x+5
print(func(5))

'''taking 2 values in lambda fn'''
func2=lambda x,y:x+y
print(func2(9,7))


"""there are map reduce and filter fn."""

l=[1,2,3,4,5]
l2=[]
for i in l:
    l2.append(i**2)
print(l2)

"""second way """

l=[1,2,3,4,5]
l2=[x**2 for x in l]
print(l2)

'''using map'''
print('map')

l=[1,2,3,4,5]
l2=list(map(lambda x:x**2,l))
print(l2)

l=[1,2,3,4,5,6,7]
l2=[]
for i in l:
    if i%2==1:
        l2.append(i)
print(l2)

l2=[x for x in l if x%2==1]
print(l2)

'''using filter'''
print('filter')
l2=list(filter(lambda x:x%2==1,l))
print(l2)

