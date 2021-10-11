# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 9:20
# @Author : zyxiao
# @File : 迭代器.py
# @Software : {PyCharm}
if __name__ == '__main__':
    mytuple = ("banana", "apple", "cherry")
    mytuple = ("banana", "apple", "cherry")
    myit=iter(mytuple)
    print(next(myit))
    print(next(myit))
    print(next(myit))
    str = "xiaohaha"
    myit = iter(str)
    print(next(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))

    for i in myit:
        print(i)
    class myNumbers:
        def __iter__(self):
            self.a = 1
            return self
        def __next__(self):
            x = self.a
            self.a += 1
            return x
    number=myNumbers()
    ha=iter(number)
    print(next(ha))
    print(next(ha))
    print(next(ha))
    print(next(ha))
    print(next(ha))

    class myNumbers():
        def __iter__(self):
            self.a = 1
            return  self
        def __next__(self):
            if self.a <= 20:
                x = self.a
                self.a += 1
                return x
            else:
                raise StopIteration
    number = myNumbers()
    myit = iter(number)
    for i in myit:
        print(i)
    def myfunc():
        x=100
        def myfunc2():
            print(x)
        myfunc2()
    myfunc()

    def myfunc():
        global a
        a = 101
    myfunc()
    print(a)
    x=999
    def myfunc():
        global x
        x =20
    myfunc()
    print(x)