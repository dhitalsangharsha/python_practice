f=open('testing.txt','w')
f.write('My name is Sangharsha \n')
for i in range(1,11):
    print(i,file=f)
f.close()

f=open('testing.txt','r')
for line in f:
    print(line.strip())
f.close()