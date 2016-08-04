import sys

Array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

class SubarryNode:
    L = 0
    R = 0
    MaxAns = 0

def FindMaxCrossingSubarray(A, low, mid, high):
    LeftSum = -sys.maxint
    sum = 0
    for i in range(mid - 1, low - 1, -1):
        sum += A[i]
        if sum > LeftSum:
            LeftSum = sum
            maxL = i

    RightSum = -sys.maxint
    sum = 0

    for i in range(mid, high):
        sum += A[i]
        if sum > RightSum:
            RightSum = sum
            maxR = i
    Ans = SubarryNode()
    Ans.R = maxR
    Ans.L = maxL
    Ans.MaxAns = LeftSum + RightSum
    return Ans

def FindMaximunSubarray(A, low, high):
    if low == high - 1:
        Ans = SubarryNode()
        Ans.L = low
        Ans.R = high
        Ans.MaxAns = A[low]
        return Ans
    else:
        mid = (low + high) / 2
#        return max(FindMaximunSubarray(A, low, mid), FindMaximunSubarray(A, mid, high), FindMaxCrossingSubarray(A, low, mid, high))
        AnsL = FindMaximunSubarray(A, low, mid)
        AnsR = FindMaximunSubarray(A, mid, high)
        AnsC = FindMaxCrossingSubarray(A, low, mid, high)
        if(AnsL.MaxAns > AnsR.MaxAns):
            if(AnsL.MaxAns > AnsC.MaxAns):
                return AnsL
            else:
                return AnsC
        else:
            if(AnsR.MaxAns > AnsC.MaxAns):
                return AnsR
            else:
                return AnsC
Ans = FindMaximunSubarray(Array, 0, len(Array))
print str.format('L:{0}, R:{1}, Max:{2}',Ans.L, Ans.R, Ans.MaxAns)