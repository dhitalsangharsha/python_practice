age_found = False
while age_found==False:
    age=input("what is your age?")
    try:
        age = int(age)
        age_found=True
        if age>=90:
            print("you should have died already")
        else:
            print("you will die in {} years".format(90-age))
    except:
        print("you can only enter numbers")