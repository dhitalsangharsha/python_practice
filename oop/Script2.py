x=[x*x for x in range(1,20)]
print("size of x:",x.__sizeof__())
#for each in x:
   # print(each)
print("*"*10)
y=(x*x for x in range(1,20))
print("size of Y:",y.__sizeof__())
#for each in y:
  #  print(each)