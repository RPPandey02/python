def Bubble_Sort(A):
    n = len(A)
    N = n-1
    for j in range(0,n):
        for i in range(0,N):
            if A[i] > A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
        N=N-1
    return A

#main
arr = [21,43,24,23,66,74,55,97,34,99]
print("sorted array is :",Bubble_Sort(arr))
