n=float(input("Enter the number of rows:"))
m=1
for i in (1,n+1):
    for j in (1,i+1):
        print(m,end=" ")
        m=m+1
    print()
