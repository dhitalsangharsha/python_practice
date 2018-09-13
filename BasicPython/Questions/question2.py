'''Write a password generator in Python. Default password
length is 8 and this default length can be modified
according to user's choice. Hint: Use the random module by importing it. import random
'''

'''questions link goo.gl/KB7d5b'''

import random
import string
s=string.ascii_letters+string.digits+string.punctuation
random.sample(s,8)

def gen_pass(length=8):
    return " ".join(random.sample(s,length))
print(gen_pass(80))

'''using loop'''

l=[]
n=int(input("enter the length of password"))
for i in range(n+1):
    l.append(random.choice(s))

'''using lambda'''
pass1=lambda length=8:"".join(random.sample(s,length))