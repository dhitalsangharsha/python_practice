def my_func():
    print("Hello World!")
def outer(arg_func):
    def inner():
        print("Innner executed")
        arg_func()
    return inner()

m=my_func #function assigned as a variable's value
o=outer
r=o(m) #passing function to another function
r() #this is executing the inner() functionn


