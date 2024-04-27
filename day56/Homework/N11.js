function isPangram(sentence) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz';
    const seenLetters = new Set();
    
    for (let char of sentence.toLowerCase()) {
        if (alphabet.includes(char)) {
            seenLetters.add(char);
        }
    }
    
    return seenLetters.size === alphabet.length;
}

console.log(isPangram("The quick brown fox jumps over the lazy dog")); 
console.log(isPangram("Hello world")); 
