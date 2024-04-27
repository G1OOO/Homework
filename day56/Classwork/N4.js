function replaceDigits(string) {
    return string.split('').map(digit => parseInt(digit) < 5 ? '0' : '1').join('');
}

console.log(replaceDigits("123456")); 
