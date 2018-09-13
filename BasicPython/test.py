import sys
import datetime
if sys.argv[1]=='--help':
    help_str='''
    This module converts temperature to
    if celcius:
    usage:python test.py --temp 30'''
    print(help_str)
elif sys.argv[1]=='--temp':
    temp=int(sys.argv[-1])
    celcius=(temp-32)*(5/9)
    print("{} deg far is {} deg celcius".format(temp,celcius))
elif sys.argv[1]=='--time':
    print(str(datetime.datetime.now()))
else:
    print("enter valid argument")
    sys.exit(0)