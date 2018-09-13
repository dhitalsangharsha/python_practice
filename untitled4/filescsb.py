f=open('data.csv','r')
for line in f:
    line=line.strip()
    cells=line.split(',')
    name=cells[0]
    age=cells[1]
    gender=cells[2]
    l=['Ram','Shyam','Gita']
    s=",".join(l)