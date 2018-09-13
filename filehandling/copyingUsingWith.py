with open("my_script.py",'r') as rp:
    data=rp.read()

with open("my_script_copy.py",'w') as wp:
    wp.write(data)
