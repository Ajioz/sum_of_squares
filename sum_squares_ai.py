def takeTestCase(numberOfCases, testCaseList=[], index=0):
    if index == numberOfCases:      #Establish a base case to stop recursion
        return testCaseList
    
    int(input("What's your integer length: "))  # Number of integers
    input_string = input("Enter the integers, separated by spaces: ")  # Read input as a string
    numbers = [int(i) for i in input_string.split()]
    
    return takeTestCase(numberOfCases, testCaseList + [numbers], index + 1)  # Recursive call to collect more test cases


def process_test_cases(testCaseList, index=0, results=[]):
    # print(f'test case list is: {len(testCaseList)} with {testCaseList}')
    # Base case: if the index reaches the length of test cases, return results
    if index == len(testCaseList):
        return results
    
    numbers = testCaseList[index]  # Unpack the current test case
    
    results.append(sum_square(numbers))  # Append the result of sum_of_squares
    
    return process_test_cases(testCaseList, index + 1, results)  # Recursive call to the next test case


def sum_square(numbers, index=0, total=0):
    if(index == len(numbers)):
        return total
    
    if(numbers[index] > 0):
        total += numbers[index] ** 2
    
    return sum_square(numbers, index+1, total) 

def main():
    numberOfCases = int(input("How many cases do you want to perform: "))  # Read number of test cases
    test_cases = takeTestCase(numberOfCases)  # Collect all test cases recursively
    results = process_test_cases(test_cases)  # Process test cases to get the results
    # print("\n".join(map(str, results)))  # Output all results
    print(f'result: {results}')

if __name__ == "__main__":
    main()  # Execute the main function
