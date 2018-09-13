def mathmatics(x):
    yield x+x
    yield x-x
    yield x*x
    yield x/x
y=mathmatics(3) #print(next(y)) 4 times
for each in y:
    print(each)

print('other way')

def mathmatics2(x):
    return [x+x,x-x,x*x,x/x]
for each in mathmatics(9):
    print(each)