#list []
#tuple()
#dictionary{}

d={'a':'apple','b':'ball','c':'cat'}
print(d,type(d))

print(d['a'])

d={1:2,2:3,3:4}
print(d[1])

d={(1,2):3,(2,3):5}
print(d)

d={2:3,2:4}
print(d[2])

d={'b':'ball','a':'apple',"c":'cat'}
for k,v in d.items():
    print("from {},comes {}".format(k,v))

    l=list(d.items())
    l.sort()
    for k,v in l:
        print("From {},comes {}".format(k,v))


        keys=list(d.keys())
        keys.sort(reverse=True)
for k in keys:
            print("from {},comes {}".format(k,d[k]))

            ####
            d={1:2,2:3}
            print(d.get(5,0))  # d[5] if 5 in d else 0

            if 5 in d:
                print(d[5])
                print(len(d))
                