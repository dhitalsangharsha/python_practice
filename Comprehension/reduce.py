from functools import reduce
nums=[47,11,42,13]
final_val=reduce(lambda x,y:x+y,nums)
print(final_val)