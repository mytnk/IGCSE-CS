#factorial number loop


n=int(input("enter a number = "))
x=1

if n==0 or n==1:
    print(1)

else:
    for i in range(1,n+1):
        x=x*i
    print(x)
