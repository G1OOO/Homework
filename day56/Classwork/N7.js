function accum(str) {
    return str.split('').map((char, index) => {
        return char.toUpperCase() + char.toLowerCase().repeat(index);
    }).join('-');
}

console.log(accum("abcd"));
console.log(accum("RqaEzty"));
console.log(accum("cwAt"));
