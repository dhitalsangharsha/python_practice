def login_required(func):
    def wrapper():
        p=input("enter your password")
        if p=='abc123':
            return func()
        else:
            print("password did not match")
    return wrapper


