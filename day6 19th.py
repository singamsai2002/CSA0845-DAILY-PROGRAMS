total=0
aggregate=0.0
for i in range(1,5):
    mark=int(input())
    total=total+mark
print('marks',total)
print('aggregate',float(total/4))
if aggregate > 75.00:
    print("distinction")
elif aggregate<75.0 and aggregate>=60:
    print('First division')
elif aggregate<60.0 and aggregate>=50:
    print('second division')
elif aggregate<50.0 and aggregate>=40:
    print('third division')
else:
    print('fail')
