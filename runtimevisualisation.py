import matplotlib.pyplot as plt
import numpy as np
import timeit
import random
import math

def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

#insertion sort runtime visualisation

nums = np.linspace(10, 2000, 15, dtype=int)
time = [timeit.timeit('insertion_sort(arr)',
                    setup='arr=list(range({})); random.shuffle(arr)'.format(n),
                    globals=globals(),
                    number=1)
         for n in nums]

algoFig = plt.figure()

plt.plot(nums, time, 'or')
coeffs = np.polyfit(nums, time, 4)
poly = np.poly1d(coeffs)

plt.plot(nums, [poly(n)for n in nums],'-b') # polynomial fit

#0(logn), 0(n*2) and 0(2^n) runtime visualisation

generalFig = plt.figure()

ns = range(1, 100)
ts = [math.log(n, 2) * 1000 for n in ns]
plt.plot(ns, ts, 'or')

ns = range(1, 100)
ts = [(n*n) for n in ns]
plt.plot(ns, ts, 'ob')

ns = range(1, 10)
ts = [math.pow(2, n)*20 for n in ns]
plt.plot(ns, ts, 'og')

plt.show()