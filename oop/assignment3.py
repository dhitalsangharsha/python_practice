n=int(input("enter number:"))
evens=list(str(each) for each in range (0,n+1) if each%2==0)
print(evens)
print(','.join(evens))
