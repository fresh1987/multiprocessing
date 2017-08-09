# coding: utf8


class mainClass(object):
    def __init__(self):
        self.a=1

class f1(mainClass):
    def __init__(self):
        mainClass.__init__(self)
        self.b=4
        print qwe



qwe = 111111111111

A = mainClass()
B = f1()



