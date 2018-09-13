'''Creating a dictionery with 3 key-value
       key1:value1
       key2:value2
       key3:value3'''

d={"a":1,"b":2,"c":3}
print(d['a'])
d["a"]=4
for k in d:
    print('{}:{}'.format(k,d[k]))

print("\n other way \n")
'''other way'''
for k,v in d.items():
    print('{}:{}'.format(k, v))