def test(x):
    if x:
        return True
    else:
        return False
print(test(1))

l=[1,2,"",4,False]
print(list(filter(test,l)))


fib=[0,1,1,2,3,5,8,13]
result=filter(lambda x:x%2==0,fib)
print(list(result))