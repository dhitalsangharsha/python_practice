class Student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def print_all(self):
        print("\nname: " + self.name + " \nage:" + str(self.age) + " \ngender:" + self.gender)

    def add_marks(self,marks):
        self.marks=marks




ram=Student('Ram',27,'M')
shayam=Student("Shayam",43,'M')
print("this is for init function",ram.name)
ram.print_all()
shayam.print_all()

ram.add_marks([90,97,100])
print(ram.marks)


