def main():

    # get number of cases
    caseNo = int(input())
    sums = []
    sums = (caseRecurse(caseNo, sums))
    printSums(caseNo, sums, 0)


def caseRecurse(caseNo, sumList):
    if (caseNo == 0):
        return sumList

    # get number of integers
    integerNo = int(input())

    # parse by removing " "'s
    numbers = input().split()

    # recurse through numbers list and add to sums list
    sum = (squareSum(integerNo - 1, numbers, 0))
    sumList.append(sum)

    return (caseRecurse(caseNo - 1, sumList))


def squareSum(integerNo, numbers, currentSum):
    if (integerNo < 0):
        return currentSum

    # Check if integerNo is within the bounds of the numbers list
    if integerNo < len(numbers) and int(numbers[integerNo]) >= 0:  # check if positive
        # square, add to running total
        currentSum += int(numbers[integerNo]) ** 2
        return squareSum(integerNo - 1, numbers, currentSum)

    else:
        return squareSum(integerNo - 1, numbers, currentSum)

# must print recursively to match output example


def printSums(caseNo, sumList, counter):
    if (counter == caseNo):
        return
    else:
        print(sumList[counter])
        return printSums(caseNo, sumList, counter + 1)


if __name__ == "__main__":
    main()
    

'''  
This Python script calculates the sum of squares of integers provided by the user across multiple test cases. Here's a breakdown of how it works:

1. **Main Function**:
   - The `main()` function starts the program by reading the number of test cases (`caseNo`).
   - It initializes an empty list `sums` to store the results.
   - It calls `caseRecurse()` to process each test case and then calls `printSums()` to print the results.

2. **Case Recursion**:
   - The `caseRecurse(caseNo, sumList)` function handles each test case recursively.
   - If `caseNo` is zero, it returns the accumulated `sumList`.
   - It reads the number of integers for the current case and then reads the integers as a list.
   - It calculates the sum of squares of the integers using `squareSum()` and appends the result to `sumList`.
   - It recursively calls itself with `caseNo - 1` to process the next test case.

3. **Square Sum Calculation**:
   - The `squareSum(integerNo, numbers, currentSum)` function computes the sum of squares of the integers.
   - It checks if `integerNo` is valid (non-negative) and if the corresponding number is positive.
   - If valid, it squares the number and adds it to `currentSum`, then calls itself with `integerNo - 1`.
   - If the number is not valid, it simply calls itself with `integerNo - 1` to skip that number.

4. **Printing Results**:
   - The `printSums(caseNo, sumList, counter)` function prints the results recursively.
   - It checks if the `counter` has reached `caseNo` and stops if so.
   - Otherwise, it prints the sum at the current `counter` index and calls itself with `counter + 1`.

5. **Execution**:
   - The script runs the `main()` function when executed directly, starting the entire process.

Overall, the code effectively manages input, processes multiple test cases, and outputs the required sums of squares in a recursive manner.'''