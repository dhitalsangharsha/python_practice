def div(x,y):
    return x/y
try:
    div(0,5)
    div(5,0)
except ZeroDivisionError as error:
    print('error')