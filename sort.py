import random
from time import time

def bubblesort(l):
    a = 0
    i = 0
    n = 0
    v = 1
    while n < len(l) - 1:
        while i < len(l) - v:
            a = l[i]
            A = l[i + 1]
            if A > a:
                l[i] = A
                l[i + 1] = a
            i += 1
        i = 0
        n += 1
        v += 1

def insertionsort(l):
    i=1
    n=0
    q=0
    while i<len(l):
        n=i-1
        k=l[i]
        while l[n]>k and n>=0:
            l[n+1]=l[n]
            n -= 1
        l[n+1]=k
        i+=1

def selectionsort(l):
    n=0
    k=0
    while n<len(l):
        i=n+1
        q=l[n]
        while i<len(l):
            if l[i]<q:
                q=l[i]
                t=i
                k+=1
            i+=1
        if k>0:
            l[t]=l[n]
            l[n]=q
        t=0
        k=0
        n+=1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

N = int(input())
l=[]
a=0
while a<N:
    a+=1
    l+= [random.randint(0, 1000)]

if __name__ == "__main__":
    for i in range(1, 9):
        n = 10 ** i
        unsorted_list = [random.randint(1, 100) for _ in range(n)]
        print("Number of elements:", n)
        start_time = time()
        bubble_sorted_list = bubblesort(unsorted_list.copy())
        print("Bubble sort time:", time() - start_time)
        start_time = time()
        insertion_sorted_list = insertionsort(unsorted_list.copy())
        print("Insertion sort time:", time() - start_time)
        start_time = time()
        selection_sorted_list = selectionsort(unsorted_list.copy())
        print("Selection sort time:", time() - start_time)
        start_time = time()
        sorted_list = sorted(unsorted_list.copy())
        print("Sorted time:", time() - start_time)
        start_time = time()

