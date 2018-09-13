'''print 1-1000 random intiger
'''
import random
randoms=(random.randint(1,1001) for _ in range(1,1001))
print(next(randoms))
print(next(randoms))
print(next(randoms))
print(next(randoms))

