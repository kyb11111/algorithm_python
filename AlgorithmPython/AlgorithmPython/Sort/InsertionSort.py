import random
print "Generate 10 numbers randomly"

def Insertion_sort(array):
    arraylen = array.count
    for j in range(1,len(array),1):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i = i-1
        array[i+1] = key

Array = []

for i in range(0,10):
    Array.append(random.uniform(1,10))

print "Array:"
for i in range(0,10):
    print Array[i]

print "After Insertion-sort"

Insertion_sort(Array)

print "Array:"
for i in range(0,10):
    print Array[i]