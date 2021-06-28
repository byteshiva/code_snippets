import sys
import multiprocessing
from multiprocessing import Process, Value

def sumcalc(sum, range_of_number):
    for i in range_of_number:
        sum.value += i
        print(i)

if __name__ == '__main__':
    print("Python version")
    print(sys.version)
    print("Version info")
    print(sys.version_info)
    print("Number of CPU:", multiprocessing.cpu_count())

    sumval = Value('d', 0.0)

    p1 = Process(target=sumcalc, args=(sumval,range(1, 11)))
    p2 = Process(target=sumcalc, args=(sumval,range(11,21)))
    p3 = Process(target=sumcalc, args=(sumval,range(21,31)))
    p4 = Process(target=sumcalc, args=(sumval,range(31,41)))
    p5 = Process(target=sumcalc, args=(sumval,range(41,51)))
    p6 = Process(target=sumcalc, args=(sumval,range(51,61)))
    p7 = Process(target=sumcalc, args=(sumval,range(61,71)))
    p8 = Process(target=sumcalc, args=(sumval,range(71,81)))
    p9 = Process(target=sumcalc, args=(sumval,range(81,91)))
    p10 = Process(target=sumcalc, args=(sumval,range(91,101)))


    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()

    print(sumval.value)