function performOperations() {
    var num1 = parseFloat(prompt("Enter the first number:"));
    var num2 = parseFloat(prompt("Enter the second number:"));
    
    var sum = num1 + num2;
    var difference = num1 - num2;
    var product = num1 * num2;
    var quotient = num1 / num2;
    
    console.log("Sum:", sum);
    console.log("Difference:", difference);
    console.log("Product:", product);
    console.log("Quotient:", quotient);
}