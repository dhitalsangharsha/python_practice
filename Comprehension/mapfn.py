def fahrenheit(T):
    return((float(9)/5)*T+32)
temp=(36.5,76,54.6)
print("first",list(map(fahrenheit,temp)))

'''defining above in lambda and map fn.'''
f=map(lambda T:((float(9)/5)*T+32),temp)
print("second",list(f))
'''usig lambda only'''

f=lambda temp:[((float(9)/5)*T+32)for T in temp]
print("third",f(temp))
