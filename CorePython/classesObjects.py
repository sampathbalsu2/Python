class Person:
    legs=2
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.email= first+'.'+last+'@gmail.com'
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    @classmethod
    def motivationMessage(cls):
        print("success never gives up on those who work hard")


emp_1=Person('Sampath','Balsu')
print(emp_1.legs)
Person.motivationMessage()
print(emp_1.email)

