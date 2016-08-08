import random

Left = lambda i: 2*i + 1
Right = lambda i: 2*i + 2
Parent = lambda i: i/2 - 1

Array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

def MaxHeapify(A, i, heapsize):
    l = Left(i)
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    r = Right(i)
    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        MaxHeapify(A, largest, heapsize)
      
def BuildMaxHeap(A):
    ArrayLen = len(A)
    for i in range(ArrayLen/2, -1, -1):
        MaxHeapify(A, i, ArrayLen)

def HeapSort(A):
    BuildMaxHeap(A)
    heapsize = len(A)
    for i in range(heapsize - 1, 0, -1):
        A[0],A[i] = A[i],A[0]
        MaxHeapify(A, 0, i)

HeapSort(Array)
print Array
