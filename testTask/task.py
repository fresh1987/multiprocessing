from multiprocessing import Pool
from multiprocessing import cpu_count
from os import linesep
from random import choice,randint
from string import ascii_letters


print(cpu_count())
import time

class mainClass(object):
    def __init_(self):
        self.count_arrs = 50
        self.count_XMLfile = 100
        self.path = raw_input("Input path to save files or press Enter to save in project directory")

    def createArr(self, arr_no):
        for i in range(self.count_XMLfile):
            file = open(self.path + linesep + 'XMLfile_' + str(i), 'w')
            ''.join(choice(ascii_letters) for i in range(15))
            randint(1,100)
            
            file.write


    def createArrs(self):
        #arrs_to_process = int(self.count_arrs/cpu_count())
        if __name__ == '__main__':
            p = Pool()
            result = p.map(self.createArr, range(self.count_arrs))
            p.close()
            p.join()

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == '__main__':
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(100000))
    p.close()
    p.join()

    print ('Pool took:', time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))

    print("Serial processing took: ", time.time()-t2)
