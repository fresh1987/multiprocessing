
from multiprocessing import Pool, Process
from time import time, sleep

def funct(a):
    for k in range(1000):
        for j in range(10000):
            a = j*(j+1)


if __name__ == "__main__":
    t1 = time()
    pool = Pool()
    m4 = pool.map(funct,range(12))
    print(time() - t1)

    t2 = time()
    list_of_process = []
    for i in range(12):
        list_of_process.append(Process(target=funct, args=(i,)))
    for i in range(12):
        list_of_process[i].start()
    for i in range(12):
        list_of_process[i].join()
    print(time() - t2)

    t3 = time()
    for i in range(12):
        funct(i)
    print (time() - t3)


    t4 = time()
    list_of_process = []
    for i in range(12):
        list_of_process.append(Process(target=funct, args=(i,)))
    for i in range(12):
        list_of_process[i].start()
        list_of_process[i].join()
    print(time() - t4)

    t5 = time()
    list_of_process = []
    for i in range(12):
        list_of_process.append(Process(target=funct, args=(i,)))
        list_of_process[i].start()
        list_of_process[i].join()
    print(time() - t5)
