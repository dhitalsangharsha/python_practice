def login_required(func):
    def wrapper():
        p=input("enter your password")
        if p=='abc123':
            return func()
        else:
            print("password did not match")
    return wrapper


@login_required
def profile():
    print("Welcome to your profile:")

if __name__=="__main__":
    profile()