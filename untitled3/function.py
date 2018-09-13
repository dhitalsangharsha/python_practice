# a=print('somthing')
# print(a,type(a))
# age= input("what is yout age?")
#
# a=None
# if a is None:
#     a=5

# def maximum(a,b):
#     '''returns the maximum value of argument'''
#     if a>b:
#         return a
#     else:
#         return b
# m = maximum(3,5)
# print('Maximum value is:',m)
#
# def maximum2(a,b):
#     if a>b:
#         print('maximum value is',a)
#     else:
#         print('maximum value is',b)
# maximum2(10,90)


# def maximum(l):
#     max = 0
#     '''return the maximum value in the list'''
#     for i in l:
#
#         if i>max:
#             max=i
#     return max
# m= maximum([1,3,4,2,4,2,6])
# print(m)
#
# '''or we can use inbuilt fn'''
# print(max([1,2,43,56,8,6]))
# a=max
# print(a,type(a))
# print(a(([1,2,4,3,])))




# def function2(a,b=None):
#     if b=None:
#         print(a)
#     else:
#     print(a+b)
# function2('hello','world')
# function2('hello')


print('sangharsha',end='')

def function3(*args,**kwargs):
    print(args)
    print(kwargs)

function3(1,2,3,a=2,b=3)

