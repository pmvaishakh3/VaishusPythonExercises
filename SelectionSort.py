#working: here the algorithm sorts an array repeatdly by finding the min element.
#it will make thefull array into 2 sub arrays and then sort 

import sys
A=[3,4,1,7,3,0,2,6]

for i in range(len(A)):
    min_idx=i
    for j in range(i+1,len(A)):
        if A[min_idx]>A[j]:
            min_idx=j
    A[i],A[min_idx]=A[min_idx],A[i]
print ("sorted Array")
for i in range(len(A)):
    print ("%d" %A[i])
