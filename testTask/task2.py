#coding: utf-8
from multiprocess import Pool, Lock, Process, Queue
import os
from random import choice,randint
from string import ascii_letters
from time import time,sleep
import zipfile


class firstTask(object):
    def __init__(self):
        self.count_zips = 50
        self.count_XMLfile = 100
        self.list_id = []

    # Get unique id list for .xml files
    def get_list_of_id(self):
        list_size = self.count_zips * self.count_XMLfile
        while len(self.list_id) < list_size:
            id = ''.join(choice(ascii_letters) for i in range(15))
            if id not in self.list_id:
                self.list_id.append(id)

    # Write XML files to Zip archive
    def createZip(self, zip_no):
        z = zipfile.ZipFile(path + 'Zip_' + str(zip_no) + '.zip', 'w')
        for i in range(self.count_XMLfile):
            file_name = 'XMLfile_' + str(zip_no) + '_' + str(i) + ".xml"
            stroka = "<root>\n\t<var name='id' value='%s'/>\n\t<var name='level' value='%s'/> \n\t<objects>\n"\
                     %(self.list_id[zip_no*self.count_XMLfile+i], randint(1,100))
            for j in range(randint(1,10)):
                stroka+="\t\t<object name='%s'>\n" %(''.join(choice(ascii_letters) for k in range(randint(5,30))))
            stroka += "\t</objects>\n</root>"
            z.writestr(file_name, stroka)
        z.close()

    # Start function for creating Zip archives
    def createZips(self):
        t1 = time()
        if __name__ == '__main__':
            self.get_list_of_id() # get set of string id
            p = Pool()
            p.map(self.createZip, range(self.count_zips))
            p.close()
            p.join()
        print('Create .zip files time = '+ str(time() - t1) +  's')


class secondTask(object):
    def __init__(self):
        # Create list of Zip-files
        self.list_of_zips = []
        for d, dirs, files in os.walk(path):
            for f in files:
                if ".zip" in f:
                    self.list_of_zips.append(f)
        self.out_csv1 = path+'csv1.csv'
        self.out_csv2 = path+'csv2.csv'

    def parse_Zip(self, nom_zip, lock, q1, q2):
        z = zipfile.ZipFile(path+self.list_of_zips[nom_zip], 'r')
        list_of_files_in_zip = z.namelist()

        id_value = []
        id_object = []
        for fname in list_of_files_in_zip:
            list_of_object = []
            for string in z.read(fname).decode("utf-8").split(os.linesep):  #decode is needed for python3
                if "name='id'" in string:
                    idp = string.split("value='")[1].split("'")[0]
                if "name='level'" in string:
                    level = string.split("value='")[1].split("'")[0]
                if "object name='" in string:
                    q2.put([idp, string.split("object name='")[1].split("'")[0]])
            q1.put([idp, level])

    def make_csv(self, lock):
        file1 = open(self.out_csv1, "w")
        file1.write("id" + ',' + "level" + '\n')
        file2 = open(self.out_csv2, "w")
        file2.write("id" + ',' + "object_name" + '\n')
        file1.close()
        file2.close()

        if __name__ == '__main__':
            list_of_process = []
            list_of_queue1 = []
            list_of_queue2 = []
            for i in range(len(self.list_of_zips)):
                list_of_queue1.append(Queue())
                list_of_queue2.append(Queue())
                list_of_process.append(Process(target=self.parse_Zip, args=(i,lock,list_of_queue1[i], list_of_queue2[i])))
            for i in range(len(self.list_of_zips)):
                list_of_process[i].start()

            file1 = open(self.out_csv1, "a")
            for i in range(len(self.list_of_zips)):
                while list_of_queue1[i].empty() is False:
                    file1.write(list_of_queue1[i].get()[0] + ',' + list_of_queue1[i].get()[1] + '\n')
            file1.close()


            '''
            file2 = open(self.out_csv2, "a")
            for i in range(len(list_of_files_in_zip)):
                for my_object in id_object[i]:
                    file2.write(id_value[i][0] + ',' + my_object + '\n')
            file2.close()
            '''





if __name__ == '__main__':
    global path
    lock = Lock()
    #path = os.path.join(raw_input("Input path to save files or press Enter to save in project directory\n"), '')
    path = os.path.join("/home/pbxadmin/2017/1", '')

    # First task: create ZIPs archives with XML files
    A = firstTask()
    A.createZips()

    # Second task: grep id, level, options from .zip to ,csv files
    t1 = time()
    B = secondTask()
    B.make_csv(lock)

    print('Create .csv files time = ' +str(time() - t1) + 's')



# 1 sleep(3) in parseZip - отрабатывае один раз. Почему????
# сделать очередь queue