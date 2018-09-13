'''no. divisible 5 and 7 between 1 to given no.'''
def test():
    n=int(input("enter a no."))
    for i in range(0, n+1):
        if i%7==0 and i%5==0:
            yield i

y = test()

for each in y:
    print(each)