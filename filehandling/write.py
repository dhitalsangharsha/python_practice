'''creating a new file'''

fp=open("new.txt",'w')
fp.write("first sentence\n")
fp.write("second sentence\n")
fp.write("third sentence\n")
fp.close()

'''reading the exiting file'''

rp=open("new.txt","r",encoding='utf-8')

'''skips 8 characters in the file'''

rp.seek(8)
data=rp.read()
print("Data",data)
fp.close()

'''appending the exiting file'''
fp=open("new.txt",'a')

'''tell fn. tells the no. of letters in the file'''

print(fp.tell())
fp.write("this is appending mode")
fp.close()

