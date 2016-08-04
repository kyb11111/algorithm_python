import sys
import random

def Merge(A,p,q,r):
    n1 = q - p
    n2 = r - q
    L=[]
    R=[]
    i = 0
    j = 0
    for i in range(0,n1):
        L.append(A[p + i])
    for j in range(0,n2):
        R.append(A[q + j])
    i = 0
    j = 0
    k = p
    for k in range(p, r):
        if (j == n2) or (i < n1 and L[i] <= R[j]):
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def MergeSort(A, p, r):
    if p < r - 1  :
        q = (p + r) / 2
        MergeSort(A, p, q)
        MergeSort(A, q, r)
        Merge(A, p, q, r)

print "Generate 10 numbers randomly"
Array = []

for i in range(0,10):
    Array.append(random.uniform(1,10))

print "Array:"
for i in range(0,10):
    print Array[i]

print "After Insertion-sort"

MergeSort(Array, 0, 10)

print "Array:"
for i in range(0,10):
    print Array[i]