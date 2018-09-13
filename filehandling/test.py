def divide(x,y):
    return x/y


try:
    print(divide(10,0))
    print(divide(10/5))
    fp=open("test.py")
    print(fp.read())
except ZeroDivisionError as error:
    print("ZeroDivisionError Occured: "+str(error))

except FileNotFoundError as error:
    print("FileNotFoundError Occured: "+str(error))
    fp.close()

except Exception as error:
    print("Exception Occured: "+ str(error))

else:
    print("When everything is right.")
    fp.close()
finally:

    print("Always executed")