function displayText() {
    var text = document.getElementById('text').value;
    var color = document.getElementById('color').value;
    var output = document.getElementById('output');
    
    output.textContent = text;
    output.style.color = color;
}