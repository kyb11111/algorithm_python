import sys

class PriorityQueue():
    
    def __init__(self):
        self.__heapsize = 0
        self.__A = []

    __Left = lambda self, i: i * 2 + 1
    __Right = lambda self, i: i * 2 + 2
    __Parent = lambda self, i: (i - 1) / 2

    def __MaxHeapify(self, i):
        l = self.__Left(i)
        if l < self.__heapsize and self.__A[l] > self.__A[i]:
            largest = l
        else:
            largest = i
        r = self.__Right(i)
        if r < self.__heapsize and self.__A[r] > self.__A[largest]:
            largest = r
        if largest != i:
            self.__A[largest], self.__A[i] = self.__A[i], self.__A[largest]
            self.__MaxHeapify(largest)

    def top(self):
        if(self.__heapsize <= 0):
            print "heap underflow"
            return
        return self.__A[0]

    def pop(self):        
        if(self.__heapsize <= 0):
            print "heap underflow"
            return
        self.__A[self.__heapsize - 1], self.__A[0] = self.__A[0], self.__A[self.__heapsize - 1]
        self.__heapsize = self.__heapsize - 1
        self.__MaxHeapify(0)

    def __insertkey(self,i, key):
        p = self.__Parent(i)
        self.__A[i] = key
        while i > 0 and self.__A[i] > self.__A[p]:
            self.__A[i], self.__A[p] = self.__A[p], self.__A[i]
            i = p
            p = self.__Parent(i)
        
    
    def insert(self,key):
        ArrayLen = len(self.__A)
        if ArrayLen == self.__heapsize:
            self.__A.append(-sys.maxint)
        else:
            self.__A[self.__heapsize] = -sys.maxint
        self.__insertkey(self.__heapsize,key)
        self.__heapsize += 1 

    def printArray(self):
        print "[",
        for i in range(0, self.__heapsize):
            print self.__A[i],
        print "]"
     
t = PriorityQueue()
t.insert(6)
t.printArray()
t.insert(14)
t.printArray()
t.insert(7)
t.printArray()
t.insert(3)
t.printArray()
t.insert(8)
t.printArray()
t.insert(20)
t.printArray()
t.insert(1)
t.printArray()

t.pop()
t.printArray()
t.pop()
t.printArray()
t.pop()
t.printArray()


t.insert(3)
t.printArray()
t.insert(8)
t.printArray()
t.insert(20)
t.printArray()
t.insert(1)
t.printArray()