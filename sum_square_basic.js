const sum_square = (numbers) => {
    return numbers.reduce((sum, number) => sum + number ** 2, 0);
}

console.log(sum_square([3, -1, 1, 14]));