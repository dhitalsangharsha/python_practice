from utils.conversation import *
print("press 'c' if you want to convert to celcius or press 'f' for farheinhight")
c=input()
if c=='c':
    t=float(input("input enter the temperature in farheniet"))
    a=convert_to_celcius(t)
    print(a)
elif c=='f':
    t = float(input("input enter the temperature in celcius"))
    a= convert_to_celcius(t)
    print(a)
else:
    print('enter f or c')