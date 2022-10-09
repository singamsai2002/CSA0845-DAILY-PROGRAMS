ch=input("Enter a character:")
n=int(input("no of times printed:"))
if n>=0 and len(ch)==1:
      for i in range(1,n+1):
          print(ch*i)
else:
    print("Invalid output")
