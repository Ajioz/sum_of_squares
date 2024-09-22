def createList(myList):
    myList = [int(i) for i in myList.split()]
    return myList

print(createList("1 2 3 4 5"))



def stringToList(word, index=0, myList=[]):
    # Establish a base case for recursion to stop
    if index == len(word):
        return myList
    
    myList.append(word[index])
    
    return stringToList(word, index+1, myList)

print(stringToList("Hello"))
print(list("Smile"))
    