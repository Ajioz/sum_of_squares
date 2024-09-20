def sum_of_squares(numbers, index=0, total=0):
    if index == len(numbers):
        return total
    current = numbers[index]
    if current >= 0:
        total += current ** 2
    return sum_of_squares(numbers, index + 1, total)

def process_test_cases(test_cases, index=0, results=[]):
    if index == len(test_cases):
        return results
    _, numbers = test_cases[index]
    results.append(sum_of_squares(numbers))
    return process_test_cases(test_cases, index + 1, results)

def collect_test_cases(n, test_cases=[], index=0):
    if index == n:
        return test_cases
    x = int(input())  # Number of integers in the test case
    numbers = list(map(int, input().split()))  # Space-separated integers
    return collect_test_cases(n, test_cases + [(x, numbers)], index + 1)

def main():
    n = int(input())  # Number of test cases
    test_cases = collect_test_cases(n)  # Collect all test cases recursively
    results = process_test_cases(test_cases)  # Process test cases to get the results
    print("\n".join(map(str, results)))  # Output all results

if __name__ == "__main__":
    main()
