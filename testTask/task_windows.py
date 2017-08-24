#coding: utf-8

# Version for windows. Without class.
from multiprocess import Pool, Lock, Manager
import os
from random import choice,randint
from string import ascii_letters
from time import time, sleep
from zipfile import ZipFile
from sys import version as py_version
from functools import partial

# Get unique id list for .xml files
def get_list_of_id(count_zips, count_XMLfile):
    list_size = count_zips * count_XMLfile
    list_id = []
    while len(list_id) < list_size:
        id = ''.join(choice(ascii_letters) for i in range(15))
        if id not in list_id:
            list_id.append(id)
    return list_id

# Write XML files to Zip archive
def createZip(list_id, path, count_XMLfile, zip_no):
    path = os.path.join(path, 'Zip_' + str(zip_no) + '.zip')
    z = ZipFile(path, 'w')
    for i in range(count_XMLfile):
        file_name = 'XMLfile_' + str(zip_no) + '_' + str(i) + ".xml"
        stroka = "<root>\n\t<var name='id' value='%s'/>\n\t<var name='level' value='%s'/> \n\t<objects>\n"\
                     %(list_id[zip_no*count_XMLfile+i], randint(1,100))
        for j in range(randint(1,10)):
            stroka+="\t\t<object name='%s'>\n" %(''.join(choice(ascii_letters) for k in range(randint(5,30))))
        stroka += "\t</objects>\n</root>"
        z.writestr(file_name, stroka)
    z.close()

# get list_of_zips in working directory
def get_list_of_zips(path):
    # Create list of Zip-files
    list_of_zips = []
    for d, dirs, files in os.walk(path):
        for f in files:
            if ".zip" in f:
                list_of_zips.append(f)
    return (list_of_zips)

# Parse zip-archive. Get id, level, options and write them into the csv-files.
def parse_Zip(lock, list_of_zips, path, out_csv1, out_csv2, nom_zip):
    z = ZipFile(path+list_of_zips[nom_zip], 'r')
    list_of_files_in_zip = z.namelist()

    # parse zip file and get id, level, options values
    id_level = []
    id_object = []
    for fname in list_of_files_in_zip:
        list_of_object = []
        for string in z.read(fname).decode("utf-8").split('\n'):  #decode is needed for python3
            if "name='id'" in string:
                idp = string.split("id' value='")[1].split("'")[0]
            if "name='level'" in string:
                level = string.split("'level' value='")[1].split("'")[0]
            if "object name='" in string:
                list_of_object.append(string.split("object name='")[1].split("'")[0])
        id_level.append([idp, level])
        id_object.append(list_of_object)

    # write id, level. options into .csv-files
    lock.acquire()
    file1 = open(out_csv1, "a")
    for i in range(len(list_of_files_in_zip)):
        file1.write(id_level[i][0] + ',' + id_level[i][1] + '\n')
    file1.close()

    file2 = open(out_csv2, "a")
    for i in range(len(list_of_files_in_zip)):
        for my_object in id_object[i]:
            file2.write(id_level[i][0] + ',' + my_object + '\n')
    file2.close()
    lock.release()


if __name__ == '__main__':
    path = ''
    if py_version[0] == '2':
        while os.path.exists(path) is False:
            path = os.path.join(raw_input("Input correct path to working directory, please\n"), '')
    else:
        while os.path.exists(path) is False:
            path = os.path.join(input("Input correct path to working directory, please\n"), '')

    # First task: create ZIPs archives with XML files
    t1 = time()
    count_zips = 50
    count_XMLfile = 100
    list_id = get_list_of_id(count_zips, count_XMLfile)  # get list of string id
    func = partial(createZip, list_id, path, count_XMLfile)
    p = Pool()
    p.map(func, range(count_zips))
    p.close()
    p.join()
    print('Create .zip files time = ' + str(time() - t1) + 's')


    # Second task: grep id, level, options from .zip to .csv files
    t1 = time()

    # create .csv files
    out_csv1 = os.path.join(path, 'csv1.csv')
    out_csv2 = os.path.join(path, 'csv2.csv')
    file1 = open(out_csv1, "w")
    file1.write("id" + ',' + "level" + '\n')
    file2 = open(out_csv2, "w")
    file2.write("id" + ',' + "object_name" + '\n')
    file1.close()
    file2.close()

    list_of_zips =  get_list_of_zips(path) # get list of zips in working directory
    i = range(len(list_of_zips))
    p = Pool()
    m = Manager()    #Manager is needed to distribute Lock to all processes
    lock = m.Lock()
    func = partial(parse_Zip, lock, list_of_zips, path, out_csv1, out_csv2)
    p.map(func, i)
    p.close()
    p.join()
    print('Create .csv files time = ' + str(time() - t1) + 's')

