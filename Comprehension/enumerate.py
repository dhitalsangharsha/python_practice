nums=[5,4,6,7,8,99]
for index,val in enumerate(nums):
    print(index,val)

'''dictionary'''

d={}
for index, val in enumerate(nums):
    d[index]=val

'''using enumerate'''

d1={index:val for each in enumerate(nums)}