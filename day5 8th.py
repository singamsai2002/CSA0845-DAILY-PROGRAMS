def is_prime(n):
    limit=int(n/2)+1
    for i in range(2,limit):
        if n%i==0:
            return False
    return True

prime=0
composite=0
limit=int(input("How many u need to check:"))
for i in range(0,limit):
    data=int(input())
    if is_prime(data):
        prime+=1
    else:
        composite+=1
print('composite count are:',composite)
print('prime count are:',prime)
