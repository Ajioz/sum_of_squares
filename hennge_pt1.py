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
    
    if(numCollection[index] > 0 and index <= (weight-1)):
        cumulative += numCollection[index] ** 2
    
    # print(f'this is weight: {weight}')
    return sum_square(numCollection, weight, index+1, cumulative)
    

def process_capture(testCaseList, index=0, result=[]):
    
    if(index == len(testCaseList)):
        return result
    

    weight, numbers = testCaseList[index]
    print(f'weight is: {weight}, numbers are: {numbers}')
    total = sum_square(numbers, weight)
    result.append(total)
    
    return process_capture(testCaseList, index + 1, result)


def main():
    number_of_iteration = int(input("Enter the number of test cases: "))
    testCaseList = input_capture(number_of_iteration)
    result = process_capture(testCaseList)
    
    for item in result:
        print(item)


if __name__ == "__main__":
    main()