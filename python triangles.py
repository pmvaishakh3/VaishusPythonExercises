

#simple pyramid
def pyran(n):
    for i in range(0,n):
        for j in range (0,i+1):
            print ("*",end="")
        print("\r")
n=5
pyran(n)

#180 pyramid printing
def pyran2(n):
    k = 2* n-2
    for i in range(0,n):
        for j in range (0,k):
            print (end=" ")

        k=k-2

        for j in range (0,i+1):
            print ("*",end="")
        print ("\r")

n=5
pyran2(n)

#pattern triangle
def triangle(n):
    k=2*n-2
    for i in range(0,n):
        for j in range (0,k):
            print(end=" ")
            
        k=k-1

        for j in range (0,i+1):
            print("*",end="")
        print("\n")


n=5
triangle(n)

#perfect triangle
j=9
for i in range(1,10,2):
    print (' ' *j+i*'*')
    j=j-1
        
