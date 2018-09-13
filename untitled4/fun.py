l=[1,3,4]
from functools import reduce
s=reduce(lambda x,y:x+y,l)
print(s)