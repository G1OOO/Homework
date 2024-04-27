function countBy(x, n) {
    let multiples = [];
    for (let i = 1; i <= n; i++) {
        multiples.push(x * i);
    }
    return multiples;
}

console.log(countBy(1, 10));
console.log(countBy(2, 5));
