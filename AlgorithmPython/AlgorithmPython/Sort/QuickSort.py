import random
Array = []

def Partition(A, p, r):
    i = p
    for j in range(p, r - 1):
        if(A[j] <= A[r - 1]):
            A[i], A[j] = A[j], A[i]
            i = i + 1
    A[i], A[r - 1] = A[r - 1], A[i]
    print A
    return i    

def QuickSort(A, p, r):
    if(p < r - 1):
        q = Partition(A, p, r)
        QuickSort(A, p, q)
        QuickSort(A, q + 1, r)

num = 30
print "Generate ",
print num,
print " numbers randomly"

for i in range(0, num):
    Array.append(random.randint(1,100))

print Array

print "QuickSort"
QuickSort(Array, 0, len(Array))

print Array