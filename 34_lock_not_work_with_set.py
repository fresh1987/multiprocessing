# coding: utf8
from multiprocess import Pool, Lock
import os
from random import choice,randint
from string import ascii_letters
from  time import time, sleep
import zipfile


class mainClass(object):
    def __init__(self):
        self.a={1,2,3,4,5,6}
    def change(self, i, lock):
        lock.acquire()
        for i in range(3):
            print("%s" % self.a.pop())
        lock.release()
    def main_change(self,lock):
        p = Pool()
        list_of_process = []

        for i in range(2):
            list_of_process.append(p.Process(target=self.change, args=(i, lock)))
        for i in range(2):
            list_of_process[i].start()
        for i in range(2):
            list_of_process[i].join()

    def printa(self):
        print(self.a)

class f1(mainClass):
    def __init__(self):
        mainClass.__init__(self)
        self.b=4
        print qwe



lock = Lock()
qwe = 111111111111

A = mainClass()
A.main_change(lock)

A.printa()

#B = f1()



