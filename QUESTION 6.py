# Question 6

# Ek function define kijiye jo ki drivers ki speed check karega. Aur ye function
# speed naam ka ek parameter lega. 1. Agar speed 70 se kam hai to ye “ok” print 
# karega.Agar driver ki speed 70 se jyaada hai to function use har 5 km ke liye 
# 1 point dega (ye 70 ko count nahi karega).example ke liye agar speed 80 hai to 
# print karega “points:2” .Agar driver ko 12 points se jyaada points milte hai to 
# function “License suspended” print karega.


def drivers(speed):
    i=0
    while i<=speed:
        if i==70:
            print("ok")
        i=i+1
num=int(input("enter the numer"))
drivers(num)









# speed =int(input("Gaadi ki speed daalo"))
# if speed==60:
#     print ("Speed kam hai")
# elif speed==30:
#     print ("Speed bahot kam hai")
# elif speed==100:
#     print ("Speed bahot fast hai")
# else:
#     print("xy")    