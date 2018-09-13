try:
    age=int("Ram")
except Exception as e:
    print(e)

try:
    age = int("Ram")
    d={'a':1,'b':2}
    print (d['c'])
except ValueError:
    print('value bigryo')
except KeyError:
    print('key bigryo')
except:
    print("aru kei bigryo")
