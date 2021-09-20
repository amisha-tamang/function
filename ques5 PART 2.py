

def check_number(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("even",a[i],b[i])
        else:
            print("not even",a[i],b[i])
        i=i+1
check_number([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])            

