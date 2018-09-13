import sys
rp=open("x.py",'r')
file=rp.read()
rp.close()

wp=open("y.py",'w')
wp.write(file)
wp.close()
sys.exit()