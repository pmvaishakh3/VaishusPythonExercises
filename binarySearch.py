def binarySearch(arr,l,r,x):
    if (r >= 1):
        mid = 1 + (r-1)/2
        
        if arr[mid] == x:
            return mid

        elif (arr[mid] > x):
            return binarySearch(arr, 1 ,mid-1 ,x)

        else:
            return binarySearch(arr, 1, mid+1, r, x)

    else:
        return -1


arr = [2,3,4,5,2,4,10]
x = 10
a = binarySearch(arr, 0 ,(len(arr))-1, x)

if a != -1:
    print ("Element present at indez %d" %a)
else:
    print ("Element is not present in array")
