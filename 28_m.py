# -*- coding: utf-8 -*-
import time, multiprocessing

def calc_square(numbers, result,v):
    v.value=5.67
    for idx, n in enumerate(numbers):
        result[idx] = n*n



if __name__ == "__main__":
    arr = [2,3,8,9]
    result = multiprocessing.Array('i', 4)
    v = multiprocessing.Value('d', 0.0)
    p1 = multiprocessing.Process(target=calc_square, args=(arr,result,v))

    p1.start()
    p1.join()


    print('outside result = ' + str(result[:]))
    print('outside result = ' + str(result))
    print(v.value)



# append в дочернем процеесе юзаь нельзя!!!
# print result - выдаст неверный вывод, надо юзать result[:]