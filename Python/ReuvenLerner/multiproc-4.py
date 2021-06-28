#!/usr/bin/env python3

from multiprocessing import Process, Value
import glob

def count_words(counter, filename):
    try:
        counter.value += len(open(filename).read())
    except IOError:
        print("\tProblem with {}".format(filename))

if __name__ == '__main__':
    word_count = Value('i', 0)

    processes = [ ]
    for filename in glob.glob('/etc/*.conf'):
        print(filename)
        p = Process(target=count_words, args=(word_count,filename))
        p.start()
        processes.append(p)

    for one_process in processes:
        one_process.join()

    print("Total = {}".format(word_count.value))


def count_words(counter, filename):
    with counter.get_lock():
        try:
            counter.value += len(open(filename).read())
        except IOError:
            print("\tProblem with {}".format(filename))

if __name__ == '__main__':
    word_count = Value('i', 0)

    processes = [ ]
    for filename in glob.glob('/etc/*.conf'):
        print(filename)
        p = Process(target=count_words, args=(word_count,filename))
        p.start()
        processes.append(p)

    for one_process in processes:
        one_process.join()

    print("Total = {}".format(word_count.value))


