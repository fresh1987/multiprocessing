from multiprocess import Pool
from multiprocessing import cpu_count
import os
from random import choice,randint
from string import ascii_letters
import time
import zipfile


class firstTask(object):
    def __init__(self):
        self.count_arrs = 50
        self.count_XMLfile = 100
        self.set_id = set()

    def get_set_of_id(self):
        set_size = self.count_arrs * self.count_XMLfile
        for i in range(set_size):
            self.set_id.add(''.join(choice(ascii_letters) for i in range(15)))
        while len(self.set_id) < set_size:
            self.set_id.add(''.join(choice(ascii_letters) for i in range(15)))
        return

    def createArr(self, arr_no):
        z = zipfile.ZipFile(path + 'Arr_' + str(arr_no) + '.zip', 'w')
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
        # Create and sort list of Arr Zip-files
        self.list_of_zips = []
        for d, dirs, files in os.walk(path):
            for f in files:
                self.list_of_zips.append(f)
        #self.list_of_files.sort()

    def parse_Zip_arr(self, nom_arr):
        z = zipfile.ZipFile(path+self.list_of_zips[nom_arr], 'r')
        #print (z.read(self.list_of_files[nom_arr]))

        list_of_files_in_zip = z.namelist()
        for fname in list_of_files_in_zip:
            list_of_object = []
            for string in open(fname, 'r').readlines():
                if "name='id'" in string:
                    string.split("value='")[1].split("'")[0]
                if "name='level'" in string:
                    string.split("value='")[1].split("'")[0]
                if "object name='" in string:
                    list_of_object.append(string.split("object name='")[1].split("'")[0])





                        #print z.read('/data.txt')

    def make_csv(self):
        p = Pool()
        #print '(len(self.list_of_files) ', range(len(self.list_of_files))
        p.map(self.parse_Zip_arr, range(len(self.list_of_zips)))
        p.close()
        p.join()


global path
#path = os.path.join(raw_input("Input path to save files or press Enter to save in project directory\n"), '')
path = os.path.join("/home/pbxadmin/2017/08.2017/08.08", '')

#B = firstTask()
#B.createArrs()

C = secondTask()
C.make_csv()

#print(os.path)

# !  Arr - not archive !!!