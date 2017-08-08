# this programm demonstrate varian with many variables sending in process

from multiprocessing import Pool
from functools import partial

def funct(arg1, arg2, value):
    return arg1 * arg2 * value


if __name__ == "__main__":
    t = [1,2,3,4]
    arg1 = 4
    arg2 = 5

    pool = Pool(processes=4)
    func = partial(funct, arg1, arg2)
    m4 = pool.map(func,t)
    print(m4)