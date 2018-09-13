from modules.my_package.login_requireed import *
from modules.my_package.random_num_generator import random_generator as rng



@login_required
def profile():
    print("profile sucessful")

if __name__=="__main__":
    profile()
    rng()