'''1. reverse list without using reverse
   2. print numbers and their counts'''
l=[1,2,3,4,1,4,7]
lr=[]
for i in l[::-1]:
    lr.append(i)
print(lr)
'''next way'''
lr=l[::-1]
print(lr)

count={}
for i in l:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for k in count:
    print('{}->{}'.format(k,count[k]))
