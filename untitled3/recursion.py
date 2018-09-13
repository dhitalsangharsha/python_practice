# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))


def power(a,b):
    r = 1
    for i in range(1 ,b+1):
        r = r*a
    return r
print(power(9,9))


def power(a,b):
    if b==0:
        return 1
    if b>=0:
        return a*power(a,b-1)
print(power(2,5))


def sum(a,b):
    if a==b:
        return b
    return a+sum(a+1,b)
print(sum(1,5 ))



