function sumMultiplesOf3And5(number) {
    if (number < 0) return 0;
    
    let sum = 0;
    for (let i = 1; i < number; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
            sum += i;
        }
    }
    return sum;
}
console.log(sumMultiplesOf3And5(10)); 
console.log(sumMultiplesOf3And5(20));
console.log(sumMultiplesOf3And5(-5));
