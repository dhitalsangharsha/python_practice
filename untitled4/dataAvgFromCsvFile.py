'''we can also do  with.open('dat.csv','r')as f: then we can write code withing tab so that we don't need f.close()'''
f=open('data.csv','r')
count=0
sum_marks=0
no_of_female=0
header=True
for line in f:
    if header:
        header = False
        continue
    line = line.strip()
    cells=line.split(',') #['1','Sangharsha','M','100']
    marks=int(cells[3])
    sum_marks+=marks
    count+=1
    if cells[2]=='F'or cells[2]=='f':
        no_of_female+=1
f.close()
print("Average marks is:",sum_marks/count)
print("Female prcentage is:",(no_of_female/count)*100)