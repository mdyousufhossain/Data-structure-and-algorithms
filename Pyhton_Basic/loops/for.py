arr = [1,2,3,4,5,'...']

for i in range(len(arr)):
    print(i, arr[i])

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    print(user,status)
    if status == 'inactive':
        del users[user]
 