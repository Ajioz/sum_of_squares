def takeTestCase(n, test_cases=None, index=0):
    if test_cases is None:
        test_cases = []  # Initialize test cases list if not provided
    # Base case: if the index reaches the number of test cases, return the collected test cases
    if index == n:
        return test_cases
    
    x = int(input("Enter the number of integers in the test case: "))  # Number of integers
    input_string = input("Enter the space-separated integers: ")  # Read input as a string
    numbers = list(map(int, input_string.split()))  # Convert the input string to a list of integers
    return takeTestCase(n, test_cases + [(x, numbers)], index + 1)  # Recursive call to collect more test cases


def process_test_cases(test_cases, index=0, results=None):
    if results is None:
        results = []  # Initialize results list if not provided
    # Base case: if the index reaches the length of test cases, return results
    if index == len(test_cases):
        return results
    _, numbers = test_cases[index]  # Unpack the current test case
    results.append(sum_of_squares(numbers))  # Append the result of sum_of_squares
    return process_test_cases(test_cases, index + 1, results)  # Recursive call to the next test case


def sum_of_squares(numbers, index=0, total=0):
    # Base case: if the index reaches the length of the list, return the total
    if index == len(numbers):
        return total
    current_number = numbers[index]  # Get the current number from the list
    if current_number >= 0:  # Only consider non-negative numbers
        total += current_number ** 2  # Add the square of the current number to total
    return sum_of_squares(numbers, index + 1, total)  # Recursive call to the next index


def main():
    n = int(input("Enter the number of test cases: "))  # Read number of test cases
    test_cases = takeTestCase(n)  # Collect all test cases recursively
    results = process_test_cases(test_cases)  # Process test cases to get the results
    print("\n".join(map(str, results)))  # Output all results

if __name__ == "__main__":
    main()  # Execute the main function
