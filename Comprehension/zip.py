z=list(zip(["a","b","c"],[1,2,3]))
print(z)

lang=["python","java","c"]
creator=["guido van rossum",'james gosling',"denis ritchi"]
my_dic={}
for key,val in zip(lang,creator):
    my_dic[key]=val
print(my_dic)
