function multiplyArrayValues(array) {
    return array.reduce((accumulator, currentValue) => accumulator * currentValue, 1);
}

console.log(multiplyArrayValues([1, 2, 3, 4]));
