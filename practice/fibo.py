a=0
b=1
print("{}   {}".format(a,b),end='\t')
for i in range(1,19):
    c=a+b
    a=b
    b=c
    print("{}\t".format(c),end='\t')
