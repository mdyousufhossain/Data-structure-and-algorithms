from math1 import doSum

def doTesting():
    assert doSum(2,2) == 4
    assert doSum(2,1) == 3
    
    
def negetiveTest():
    assert doSum(-10,-14) == -24
    assert doSum(-3,10)  == 7
    
    
    
negetiveTest()
doTesting()