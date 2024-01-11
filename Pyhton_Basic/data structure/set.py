set = {2,3,4,5,6,7}
set2 = {2,3,4,5,6,7,8,9,1}
#print(2 in set)
 
def removeItem(item,list):
        if(item in list):
            list.remove(item)
            print(item,'removed from', list)
        #it will prevent the error we fear using this amazing feature 
        elif(item not in list):
                print(item , 'is not in the', list)
    
#remove() takes two parameter one is value other is set / array 
union_set = set | set2 #combile the both item
intersection = set & set2 # only common in both
difference_set = set - set2 # only difference in both
symmetric_difference_set = set ^ set2 # different in both
#removeItem(3,set)
# removeItem(5,set)
# removeItem(5,set)
print(set,set2)
print(symmetric_difference_set)