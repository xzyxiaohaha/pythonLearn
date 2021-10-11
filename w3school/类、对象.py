# -*- codeing = utf-8 -*-
# @Time : 2021/10/9 14:57
# @Author : zyxiao
# @File : 类、对象.py
# @Software : {PyCharm}
class myClass:
    x=5

if __name__ == '__main__':
    p1 = myClass()
    print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+self.name)
    def myfunc2(this):
        print("show me",this.age)
p1=Person("Bill",12)
print(p1.name)
print(p1.age)
p1.myfunc()
p1.age=14
# print(p1.age)
# del p1.age
# print(p1.age)
p1.myfunc2()
class Person:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    def printName(self,flag):
        print("this is Person printName()")
        print(flag+"firstName:"+self.firstName+"lastName"+self.lastName)

x=Person("xiaohaha","xiaozhenyu")
x.printName("哈哈哈")
class Student(Person):
    def __init__(self,firstName,lastName):
        Person.__init__(self,firstName,lastName)
        print("进入Student")
x=Student("123","456")
x.printName("啦啦啦")
class Student(Person):
    def __init__(self,firstName,lastName):
        super().__init__(firstName,lastName)
        self.graduationYear=2024
x=Student("123","456")
print(x.graduationYear)

class Student(Person):
    def __init__(self, firstName, lastName, graduationYear):
        super().__init__(firstName,lastName)
        self.graduationYear=graduationYear
    def welcome(self):
        print("welcome:",self.firstName,self.lastName,"your graduaion year is:",self.graduationYear)
    def printName(self,flag):
        print("this is Student printName()")
x=Student("123","456","2024")
x.printName("show")
x.welcome()