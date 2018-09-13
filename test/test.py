primes=[]
with open("primenumbers.txt",'r') as rp1:
    lines=rp1.readlines()
    for each in lines:
        primes.append(int(each))
primes=set(primes) #'''converting list into set'''

happy=[]
with open("happynumbers.txt",'r') as rp2:
    lines=rp2.readlines()
    for i in lines:
        happy.append(int(i))
happy=set(happy)

overlap=primes.intersection(happy)
print(overlap)