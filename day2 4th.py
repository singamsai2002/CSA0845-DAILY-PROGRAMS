listone = []
listtwo = []
print("enter 3 elements for first list:")
for i in range(6):
    listone.append(input())
print("enter 3 elements for second list:")
for i in range(6):
    listtwo.append(input())

listthree = []
for i in range(6):
    listthree.append(listone[i])
for i in range(6):
    listthree.append(listtwo[i])
print("the new (merged) list is:")
print(listthree)
