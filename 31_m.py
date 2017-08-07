def f(n):
    return n*n

if __name__ == '__main__':
    array = [1,2,3,4,5]

    result = []
    for i in array:
        result.append(f(i))

    print result


# !!!!!!!!!!!!!! MAKE printscreen 1 and insert them in the presentation


from multiprocessing import Pool
import time


def f(n):
    sum = 0
    for x in range(10000):
        sum += x*x
    return sum

if __name__ == '__main__':
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(10000))
    p.close()
    p.join()

    print ('Pool took:', time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(10000):
        result.append(f(x))

    print("Serial processing took: ", time.time()-t2)

#    results:
#    [1, 4, 9, 16, 25]
#    ('Pool took:', 2.918668031692505)
#    ('Serial processing took: ', 5.801117897033691)

# !!!!!!!!!!!!!! MAKE printscreen 2 and insert them in the presentation

# !!!! printscreen c task managera (5 process on 4-core proccess)

