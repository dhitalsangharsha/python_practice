fp=open("birthday.txt")
data=fp.read()
passed_data=eval(data)
name=input("enter name:")
print(passed_data.get(name))