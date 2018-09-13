'''to import function name sum_to_n from file fn to test file '''

from fn import sum_to_n
'''if we want to import other fn from file then we can seprate it by comma'''
print(sum_to_n(5))

'''other way to import'''

from fn import *
'''importing all functions of file'''

print(sum_to_n(9))



import fn
'''importing file itself'''
print(fn.sum_to_n(9))