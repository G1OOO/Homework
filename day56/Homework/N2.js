function blankPagesNeeded(n, m) {
    if (n < 0 || m < 0) {
        return 0;
    } else {
        return n * m;
    }
}

console.log(blankPagesNeeded(5, 5));
console.log(blankPagesNeeded(-5, 5));
