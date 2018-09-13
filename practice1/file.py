'''1: create a file which has the following text:
1x1=1 2x1=1
1x2=2  2x2=2 and so on upto 10'''
with open("multipication_table.txt",'w') as fp:
    for i in range(1,11):
        for j in range(1,3):
         print("{} x {} ={} ".format(j,i,i*j),end="\t", file=fp)

        print("\n", file=fp)

'''column outer loop and row should be in inner loop'''