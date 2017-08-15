import time
import  multiprocessing

square_result = []

def calc_square(numbers):
    global square_result
    for n in numbers:
        #time.sleep(2)
        print('square ' + str(n*n))
        square_result.append(n*n)
    print('Proccesses result are' + str(square_result))

def calc_cube(numbers):
    for n in numbers:
        #time.sleep(2)
        print ('cube' + str(n*n*n))


if __name__ == "__main__":
    arr = [2,3,8,9]
    arr = range(2000000)
    p1 = multiprocessing.Process(target=calc_square, args=(arr, ))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr, ))
    p3 = multiprocessing.Process(target=calc_square, args=(arr, ))
    p4 = multiprocessing.Process(target=calc_cube, args=(arr, ))
    p5 = multiprocessing.Process(target=calc_cube, args=(arr, ))
    p6 = multiprocessing.Process(target=calc_square, args=(arr, ))
    p7 = multiprocessing.Process(target=calc_cube, args=(arr, ))



    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()


    print('result' + str(square_result))
    print('Done')
