


# add_numbers_list naam ka function likhiye jo do integers ki 
# 2 lists leta ho aur fir same position wale integers ka sum print karta ho. 
# Same position waale 2 integers ka sum karne ke liye Part 1 mein di gayi add_
# numbers waale function ka use karo. Jaise agar hum iss function ko [50, 60, 10] 
# aur [10, 20, 13] denge ko woh yeh print karega



def add_number_list():
    var1 = [50, 60, 10]
    var2 = [10, 20, 13]
    i=0
    t=[]
    while i<len(var1):
        if var1[i] and var2[i]:
            var=var1[i]+var2[i]
            t.append(var)
        i=i+1
    print(t)
            
add_number_list()    







