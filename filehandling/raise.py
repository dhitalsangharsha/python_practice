def divide(x,y):
    if y==0:
        raise Exception ("denominator can't be zero")
    return x/y

def get_file(file_name):
    try:
        fp=open(file_name)
    except:
        raise FileNotFoundError("File you are looking is not found")
    return fp.read()

try:
    print(divide(5,3))
    print(divide(6,4))
except Exception as e:
    print(e)

