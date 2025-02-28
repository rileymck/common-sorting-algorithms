"""
Assignment 2: Bubble Sort, Insertion Sort, Merge Sort, Hybrid Sort, Quick Sort, Radix Sort
Author: Riley McKenzie

This program implements 6 sort algorithms:
1. Bubble Sort
2. Insertion Sort
3. Merge Sort
4. Hybrid Sort
5. Quick Sort
6. Radix Sort
"""


import time
import random
import sys

sys.setrecursionlimit(500000)


def bubbleSort(alist):
    """Sort a list using the bubble sort algorithm."""
    start_time = time.time()

    n = len(alist)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]  # Swap elements
                swapped = True
        if not swapped:
            break  # Stop if no swaps occurred

    elapsed_time = time.time() - start_time
    return (alist, elapsed_time)


def insertionSort(alist):
    """Sort a list using the insertion sort algorithm."""
    start_time = time.time()

    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key

    elapsed_time = time.time() - start_time
    return (alist, elapsed_time)


def mergeSort(alist):
    """Sort a list using the merge sort algorithm."""
    start_time = time.time()

    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1

    elapsed_time = time.time() - start_time
    return (alist, elapsed_time)


def hybridSort(alist):
    """Sort a list using the hybrid sorting algorithm."""
    start_time = time.time()

    if len(alist) <= 10:
        for i in range(1, len(alist)):
            key = alist[i]
            j = i - 1
            while j >= 0 and alist[j] > key:
                alist[j + 1] = alist[j]
                j -= 1
            alist[j + 1] = key
    else:
        if len(alist) > 1:
            mid = len(alist) // 2
            left_half = alist[:mid]
            right_half = alist[mid:]

            hybridSort(left_half)
            hybridSort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    alist[k] = left_half[i]
                    i += 1
                else:
                    alist[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                alist[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                alist[k] = right_half[j]
                j += 1
                k += 1

    elapsed_time = time.time() - start_time
    return (alist, elapsed_time)


def quickSort(alist, pivot='first'):
    """Sort a list using the quick sort algorithm."""
    start_time = time.time()

    if len(alist) <= 1:
        elapsed_time = time.time() - start_time
        return alist, elapsed_time

    if pivot == 'first':
        pivot_value = alist[0]
    elif pivot == 'middle':
        pivot_value = alist[len(alist) // 2]
    else:
        pivot_value = alist[0]

    left = [x for x in alist if x < pivot_value]
    middle = [x for x in alist if x == pivot_value]
    right = [x for x in alist if x > pivot_value]

    sorted_list = quickSort(left, pivot)[0] + middle + quickSort(right, pivot)[0]

    elapsed_time = time.time() - start_time
    return sorted_list, elapsed_time


def radixSort(alist):
    """Sort a list using the radix sort algorithm."""
    start_time = time.time()

    if len(alist) == 0:
        elapsed_time = time.time() - start_time
        return alist, elapsed_time

    max_num = max(alist)
    exp = 1

    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]

        for num in alist:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        alist = [num for bucket in buckets for num in bucket]
        exp *= 10

    elapsed_time = time.time() - start_time
    return alist, elapsed_time


if __name__ == '__main__':
    def testFunction(sort_function, alist):
        """Test utility function."""
        alist2 = alist.copy()
        res = sort_function(list(alist))
        print(f"Using {sort_function.__name__} to sort list: {alist[:10]}... w/ {len(alist)} items")
        print(f"    sort time: {res[1]:.4f} seconds")
        alist2.sort()
        print(f"    sorted correctly?: {'y :)' if res[0] == alist2 else 'n :('}")

    list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    testFunction(bubbleSort, list(list1))
    testFunction(insertionSort, list(list1))
    testFunction(mergeSort, list(list1))
    testFunction(hybridSort, list(list1))
    testFunction(quickSort, list(list1))
    testFunction(radixSort, list(list1))

    random.seed(1)
    list2 = list(range(5000))
    random.shuffle(list2)
    testFunction(bubbleSort, list(list2))
    testFunction(insertionSort, list(list2))
    testFunction(mergeSort, list(list2))
    testFunction(hybridSort, list(list2))
    testFunction(quickSort, list(list2))
    testFunction(radixSort, list(list2))

    list3 = list(range(6000, 1000, -1))
    testFunction(bubbleSort, list(list3))
    testFunction(insertionSort, list(list3))
    testFunction(mergeSort, list(list3))
    testFunction(hybridSort, list(list3))
    testFunction(quickSort, list(list3))
    testFunction(radixSort, list(list3))
