from multiprocess import Pool
from multiprocessing import cpu_count
import os
from random import choice,randint
from string import ascii_letters
import time
import zipfile

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
        z = zipfile.ZipFile(self.path + 'Arr_' + str(arr_no), 'w')
        for i in range(self.count_XMLfile):
            file_name = 'XMLfile_' + str(arr_no) + ' ' + str(i)
            stroka = "<root>\n\t<var name='id' value='%s'/>\n\t<var name='level' value='%s'/> \n\t<objects>\n" %(self.set_id.pop(), randint(1,100))
            for j in range(randint(1,10)):
                stroka+="\t\t<object name='%s'>\n" %(''.join(choice(ascii_letters) for k in range(randint(5,30))))
            stroka += "\t</objects>\n</root>"
            z.writestr(file_name, stroka)
        z.close()
        return

    def createArrs(self):
        t1 = time.time()
        if __name__ == '__main__':
            self.get_set_of_id() # get set of string id
            p = Pool()
            p.map(self.createArr, range(self.count_arrs))
            p.close()
            p.join()
        print time.time() - t1


class secondTask(object):
    def __init__(self):
        pass
    def 


A = mainClass()
A.createArrs()

#print(os.path)

