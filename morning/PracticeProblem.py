'''Given
two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file
has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
# Handle cases for FileNotFoundError.'''
primes=[]
with open("one.txt",'r') as rp1:
    lines=rp1.readlines()
    for each in lines:
        primes.append(each)
primes=set(primes) #'''converting list into set'''

happy=[]
with open("happynumbers.txt",'r') as rp2:
    lines=rp2.readlines()
    for i in lines:
        happy.append(i)
happy=set(happy)

overlap=primes.intersection(happy)
print(overlap)

fp = open("primenumbers.txt")
print(fp.read())