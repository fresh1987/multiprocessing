from multiprocess import Pool
from multiprocessing import cpu_count
import os
from random import choice,randint
from string import ascii_letters
import time

print(cpu_count())

class mainClass(object):
    def __init__(self):
        self.count_arrs = 50
        self.count_XMLfile = 100
        #self.path = os.path.join(raw_input("Input path to save files or press Enter to save in project directory\n"), '')
        self.path = os.path.join("/home/pbxadmin/2017/08.2017/08.08", '')
        self.set_id = set()

    def get_set_of_id(self):
        set_size = self.count_arrs * self.count_XMLfile
        for i in range(set_size):
            self.set_id.add(''.join(choice(ascii_letters) for i in range(15)))
        while len(self.set_id) < set_size:
            self.set_id.add(''.join(choice(ascii_letters) for i in range(15)))
        return


    def createArr(self, arr_no):
        time.sleep(1)
        for i in range(self.count_XMLfile):
            file_name = self.path + 'XMLfile_' + str(arr_no) + ' ' + str(i)
            file = open(file_name, 'w')
            stroka = "<root>\n\t<var name='id' value='%s'/>\n\t<var name='level' value='%s'/> \n\t<objects>\n" %(self.set_id.pop(), randint(1,100))
            for j in range(randint(1,10)):
                stroka+="\t\t<object name='%s'>\n" %(''.join(choice(ascii_letters) for k in range(randint(5,30))))
            stroka += "\t</objects>\n</root>"
            file.write(stroka)
            file.close()
        return arr_no


    def createArrs(self):
        #arrs_to_process = int(self.count_arrs/cpu_count())
        t1 = time.time()
        if __name__ == '__main__':
            self.get_set_of_id() # get set of string id
            p = Pool()
            result = p.map(self.createArr, range(self.count_arrs))
            p.close()
            p.join()
        print time.time() - t1

A = mainClass()
A.createArrs()



def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == '__1main__':
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
