myUniqueList = []
myLeftovers = []

def List(new):
  if new not in myUniqueList:
    myUniqueList.append(new)
    return True
  else:
    myLeftovers.append(new)
    return False
    
List(22)
List(45)
List(56)
List(11)
List(45)
List(72)
List(11)
List(67)
List(22)
  
print (myUniqueList)
print (myLeftovers)