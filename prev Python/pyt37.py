a=[]
n=int(input("Enter N o E: "))
for i in range(1,n+1):
    b=int(input("Enter element: "))
    a.append(b)
a.sort()
print("largest element is:",a[n-1])

