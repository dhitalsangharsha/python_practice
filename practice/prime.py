def prime(n):
    #n=int(input("enter a no."))
    for i in range(2,(n//2)+1):
        if n%i==0:
            print("{} is not a prime no.".format(n))
            return
    print ("{} is a prime no.".format(n))

prime(17)