class TooYoungeException(Exception):
    def __init__(self,arg):
        self.msg=arg

class TooOldException(BaseException):
    def __init__(self,arg):
        self.msg=arg
age=int(input("Enter age :"))
if age>60:
    raise TooYoungeException("Plz wait some more time definately you will get best match soon")
elif age<18:
    raise TooOldException("Ur age already crossed marriage age no chance of getting marriage")
else:
    print("Thanks for registration")