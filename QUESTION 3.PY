# Question 3


# Ek function banaiye jo 3 numbers ka sum aur average print kare.
# Hum user se 3 number input karwayenge aur fir unn 3 numbers ka sum aur average 
# print karwayenge jaisa ki niche output diya hua hain.


def num_list():
    a=[3,4,5]
    i=0
    sum=0
    avg=0
    while i<len(a):
        sum=sum+a[i]
        i=i+1
    avg=sum/3
    print(sum)
    print(avg)
num_list()    

