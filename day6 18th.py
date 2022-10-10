data =[85,45,65,75,95]
m=int(input("Enter the m value:"))
n=int(input("Enter the n value:"))
data.sort()
print(m,"maximum no is:",data[m-1])
print(n,"minimum no is:",data[len(data)-n])
print('sum is:',data[m-1]+data[len(data)-n])
