def sum_square(numbers, index=0, total=0):
    if(index == len(numbers)):
        return total
    
    if(numbers[index] > 0):
        total += numbers[index] ** 2
    
    return sum_square(numbers, index+1, total) 


print(f'sum of hte square of given list is: {sum_square([3, -1, 1, 14])}')