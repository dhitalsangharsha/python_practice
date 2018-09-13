# for i in range (1,6):
#     for j in range(1,i+1):
#         print (j,end=' ')
#     print ()
#
#
# print("Sangharsha",end=' ')
# print("Dhital")

s=int(input("enter the starting point of prime no."))
e=int(input("enter the end point of prime np."))
for j in range(s,e):
    is_prime =True
    for i in range(2,int(((s+e)/2))):
        if j%i=0:
            print(i)

