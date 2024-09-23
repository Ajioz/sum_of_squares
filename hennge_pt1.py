def input_capture(number_of_iteration, index=0, testCaseList=[]):
    
    # Establish a base case for recursion termination
    if(index == number_of_iteration):
        return testCaseList
    
    #Get the weight of the iteration, which would be used to detemine how deep to sum numbers
    depth_of_sum = int(input("Enter size of iterable: ")) 
    # now collect user numbers list separated by comma  
    numbers = input("Enter list of numbers, separated by spaces: ")
    
    # using list comprehension to gets list of numbers
    iterable = [int(i) for i in numbers.split()]
    # make it into tuple to capture weight
    testCaseList.append((depth_of_sum, iterable))
    
    # Recursive call to the next test case
    return input_capture(number_of_iteration, index + 1, testCaseList)
    
    
def sum_square(numCollection, weight, index=0, cumulative=0):
    # Establish a base case for recursion termination
    if(index == len(numCollection)):
        return cumulative
    
    # check if its not negative value and the index does not exceed the weight 
    if(numCollection[index] > 0 and index <= (weight-1)):
        cumulative += numCollection[index] ** 2
    
    # Recursive call to the next test case
    return sum_square(numCollection, weight, index+1, cumulative)
    

def process_capture(testCaseList, index=0, result=[]):
    
    # Establish a base case for recursion termination
    if(index == len(testCaseList)):
        return result
    

    # tuple un-packing to receive list of numbers and it respective weight
    weight, numbers = testCaseList[index]
    print(f'weight is: {weight}, numbers are: {numbers}')
    
    # invoke the sun_square helper method
    total = sum_square(numbers, weight)
    result.append(total)
    
    # Recursive call to the next test case
    return process_capture(testCaseList, index + 1, result)


def main():
    # Begin in the main loop to track the number of test case
    number_of_iteration = int(input("Enter the number of test cases: "))
    # invoke the input collection while leveraging on the number of iteration
    testCaseList = input_capture(number_of_iteration)
    # invoke the process capture while leveraging on the testCaseList 
    result = process_capture(testCaseList)
    
    # output final result
    for item in result:
        print(item)


if __name__ == "__main__":
    main()
    
