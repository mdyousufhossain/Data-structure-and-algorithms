a,b = 0,1 

while a < 50: 
     print(a)
     a,b = b , a + b
     


while a > 0:
    print(a)
    a, b = b - a, a

     
     
     
# a = 0 , b = 1 , until a reach 100 we will sum value  
# so first value of a = 0 but b is 1 
# so lets explain

# ---------------------- 
#(previus value of 'a' sum new value of'b' )
# a = 0 , b = 1  
# a = 1  b = 1 ,b= 0 + 1
# a = 1  b = 1 ,b= 1 + 1  
# a = 2  b = 2 ,b= 1 + 2
# a = 3  b = 3 ,b= 2 + 3
# a = 5  b = 5 ,b= 3 + 5
# a = 8  b = 8 ,b= 5 + 8
# a = 13 b = 13,b= 8 + 13
# a = 21 b = 21,b= 13 + 21
# a = 34  
 
# c , d = 0 , 1 

# while c < 50:
#      print(c)
#      c , d = d , c + d 
 
# c = 0
# while c < 20:
#      print(c)
#      c += 1   
    