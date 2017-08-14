#coding: utf-8
from multiprocess import Pool, Lock
import os
from random import choice,randint
from string import ascii_letters
from time import time,sleep
import zipfile



class firstTask(object):
    def __init__(self):
        self.count_arrs = 50
        self.count_XMLfile = 100
        self.list_id = []

    def get_set_of_id(self):
        set_size = self.count_arrs * self.count_XMLfile
        while len(self.list_id) < set_size:
            id = ''.join(choice(ascii_letters) for i in range(15))
            if id not in self.list_id:
                #print id
                self.list_id.append(id)

    def createArr(self, arr_no):
        z = zipfile.ZipFile(path + 'Arr_' + str(arr_no) + '.zip', 'w')
        for i in range(self.count_XMLfile):
            file_name = 'XMLfile_' + str(arr_no) + '_' + str(i) + ".xml"
            stroka = "<root>\n\t<var name='id' value='%s'/>\n\t<var name='level' value='%s'/> \n\t<objects>\n"\
                     %(self.list_id[arr_no*self.count_XMLfile+i], randint(1,100))
            for j in range(randint(1,10)):
                stroka+="\t\t<object name='%s'>\n" %(''.join(choice(ascii_letters) for k in range(randint(5,30))))
            stroka += "\t</objects>\n</root>"
            z.writestr(file_name, stroka)
        z.close()

    def createArrs(self):
        t1 = time()
        if __name__ == '__main__':
            self.get_set_of_id() # get set of string id
            p = Pool()
            p.map(self.createArr, range(self.count_arrs))
            p.close()
            p.join()
        print time() - t1


class secondTask(object):
    def __init__(self):
        # Create and sort list of Arr Zip-files
        self.list_of_zips = []
        for d, dirs, files in os.walk(path):
            for f in files:
                if ".zip" in f:
                    self.list_of_zips.append(f)
        #self.list_of_files.sort()
        self.out_csv1 = path+'csv1.csv'
        self.out_csv2 = path+'csv2.csv'

    def parse_Zip_arr(self, nom_arr, lock):
        z = zipfile.ZipFile(path+self.list_of_zips[nom_arr], 'r')
        list_of_files_in_zip = z.namelist()

        id_value = []
        id_object = []
        for fname in list_of_files_in_zip:
            list_of_object = []
            for string in z.read(fname).split(os.linesep):
                if "name='id'" in string:
                    idp = string.split("value='")[1].split("'")[0]
                if "name='level'" in string:
                    level = string.split("value='")[1].split("'")[0]
                if "object name='" in string:
                    list_of_object.append(string.split("object name='")[1].split("'")[0])
            id_value.append([idp, level])
            id_object.append(list_of_object)

        lock.acquire()
        file1 = open(self.out_csv1, "a")
        for i in range(len(list_of_files_in_zip)):
            file1.write(id_value[i][0] + ',' + id_value[i][1] + '\n')
        file1.close()

        file2 = open(self.out_csv2, "a")
        for i in range(len(list_of_files_in_zip)):
            for my_object in id_object[i]:
                file2.write(id_value[i][0] + ',' + my_object + '\n')
        file2.close()
        lock.release()

    def make_csv(self, lock):
        file1 = open(self.out_csv1, "w")
        file1.write("id" + ',' + "level" + '\n')
        file2 = open(self.out_csv2, "w")
        file2.write("id" + ',' + "object_name" + '\n')
        file1.close()
        file2.close()

        p = Pool()
        list_of_process = []
        for i in range(len(self.list_of_zips)):
            list_of_process.append(p.Process(target=self.parse_Zip_arr, args=(i,lock)))
        for i in range(len(self.list_of_zips)):
            list_of_process[i].start()
        for i in range(len(self.list_of_zips)):
            list_of_process[i].join()




global path
lock = Lock()
t1 = time()
#path = os.path.join(raw_input("Input path to save files or press Enter to save in project directory\n"), '')
path = os.path.join("/home/pbxadmin/2017/08.2017/08.08", '')

B = firstTask()
B.createArrs()

C = secondTask()
C.make_csv(lock)

print(time() - t1)



# !  Arr - not archive !!!
