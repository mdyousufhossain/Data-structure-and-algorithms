# classes can be explain as cookie cutter :)

class Cookie: # use capital its good practice
    def __init__(self,color): # __init__ is a build in class method aka constr
        self.color = color  
        
        
class Human:
    def __init__(self,value):
        self.value = value
        
    def setGender(self,value):
        if(self.value == 'male' | self.value == 'female'):
            self.value = value
        else : 
            return 'there no gender beside male and female'
        
    def setGender(self,value):
        
             self.value = value 
        
    

    def setName(self,value):
        self.value = value
            
            
    def getName(self):
            return self.value 
    
    


metahuman = Human.setName('bal','heda')
metahuman1 = Human.getName

print(metahuman1)
        