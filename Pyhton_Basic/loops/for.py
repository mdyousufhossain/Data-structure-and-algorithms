arr = {}



# for i in range(len(arr)):
#     print(i, arr[i])

# user = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# for user, status in users.copy().items():
#     #print(user,status)
#     if status == 'inactive':
#         del users[user]
 
print(len(arr) > 0)
val = 0

while len(arr) < 7:
    val += 1
    arr.append(val)


# print(len(arr))
arr.extend([3,12,67])
val1 = 0

for i in arr:
    val1 += i
    print(val1) 
    
val3 = 0 
for i in range(len(arr)):
    print('this is normal array :', arr[i])
    val3 += arr[i]
    print('this is value after sum : ', val3)
    
print(val1 == val3)    

print('this is content of value 3 : ',val3)

print(arr)     



    
    



