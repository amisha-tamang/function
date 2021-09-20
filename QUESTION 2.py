        


def ek_perfect():
    i=1
    sum=0
    n=int(input("enter the number"))
    while i<n:
        if n%i==0:
            sum=sum+i
        i=i+1
    if n==sum:
        print("it is prefect number")
    else:
        print("it is not prefect number")
ek_perfect()            

