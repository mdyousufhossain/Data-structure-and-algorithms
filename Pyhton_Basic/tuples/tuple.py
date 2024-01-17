tup = (1,'string',True,5.52,['name','age','grade']) # tuple can store many different types of items

#print(tup)  
tup[-1].append('newitem') # you can appeend within touple an array
tup[-1][0] = 'it can be change' # you can use array all beneit within the touples
#print(tup)

# converting the  tuple to array

convertedtuples =  list(tup) # you can convert items to the list using built in list funciton
# you can use shallow copy technic
convertedtuples.append('adding item to the tuple')
convertedtuples = tuple(convertedtuples) # converting list to the tuple again 
#print(tup,convertedtuples)

# unpacking the tuple 

a , b , bal , sal , *c = tup #this method called tuples unpacking 

usingDic = {'fist' : a , 'second':b , 'third':bal,'forth':sal , 'rest':c }

#print(usingDic)

#looping over tuple

tuplesNum = (1,2,3,4,5,6,7)


print(len(tuplesNum) > 6 )  

val3 = 0 # sum of tuples items
for i in range(len(tuplesNum)):
    val3 += tuplesNum[i]
    #print(val3)
    


#using tuples as a dic 

employee_salaries = {('John', 'Doe', 'Manager'): 75000, ('Jane', 'Smith', 'Developer'): 60000}

#dic key are immutable so are the tuples thats why using tuples as key is a good practice 

#print(employee_salaries)
    








