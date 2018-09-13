rp=open("my_file.py",'r')
program=rp.read()
rp.close()

wp=open("my_file_copy.py",'w')
wp.write(program)
wp.close()