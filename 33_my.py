# Work multiprocess with CLASS function

from multiprocess import Pool, TimeoutError, cpu_count

class MyClass:
    def square(self, x):
        return x*x

    @staticmethod
    def getNumbers():
        return range(10)

    def calculate(self):
        pool = Pool(processes=min(cpu_count(),8))
        results = [pool.apply(self.square,(i,)) for i in self.getNumbers()]
        pool.close()
        pool.join()
        for result in results:
            print result


if __name__ == '__main__':
    instance = MyClass()
    instance.calculate()