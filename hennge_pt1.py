


def input_capture(number_of_iteration, index=0, testCaseList=[]):
    
    # Establish a base case for recursion termination
    if(index == number_of_iteration):
        return testCaseList
    
    depth_of_sum = int(input("Enter size of iterable: "))
    numbers = input("Enter list of numbers, separated by spaces: ")
    
    iterable = [int(i) for i in numbers.split()]
    testCaseList.append((depth_of_sum, iterable))
    
    # Recursive call to the next test case
    return input_capture(number_of_iteration, index + 1, testCaseList)
    
def sum_square(myList, index=0, result=0):
    # Establish a base case for recursion termination
    if(index == len(myList)):
        return result
    
    if(myList[index] > 0):
        result =+ myList[index] **2
    
    return sum_square(myList, index+1, result)
    

def process_capture(testCaseList, index=0, result=[]):
    
    if(index == len(testCaseList)):
        return result
    

    weight, numbers = testCaseList
    print(weight, numbers)
    
    return process_capture(testCaseList, index + 1, )


def main():
    number_of_iteration = int(input("Enter the number of test cases: "))
    testCaseList = input_capture(number_of_iteration)
    result = process_capture(testCaseList)
    
    for item in result:
        print(item)




if __name__ == "__main__":
    main()