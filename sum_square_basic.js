const sum_square = (numbers) => {
    return numbers.reduce((sum, number) => sum + number ** 2, 0);
}

console.log(sum_square([3, -1, 1, 14]));

const sum_squarev2 = (numbers, index = 0, total=0) => {
    if (index === numbers.length) return total;
    if (numbers[index] > 0) total += numbers[index] ** 2
    return sum_squarev2(numbers, index+1, total)
};

console.log(sum_squarev2([3, -1, 1, 14]));