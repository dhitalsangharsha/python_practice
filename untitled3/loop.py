# l=[1,2,3,4,5]
# for i in l:
#     print(i)

#to print all natural no.s upto 100
for i in range(1,101):
     print (i)

     print(type(range(1,101)))

#creating list
     l=list(range(1,100))
     print(l,type(l))


#to print all odd numbers upto 100

for i in range(1, 101,2):
     print(i)

#nested for creating multiplication table

for i in range(1,5):
    for j in range(1,5):
        print('{} x {} ={}'.format(j,i,i*j),end="\t")
    print('\n')

#print the output of *

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='\t')
    print()