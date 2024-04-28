function changeDivProperties() {
    var bgColor = document.getElementById("bgColor").value;
    var width = document.getElementById("width").value;
    var height = document.getElementById("height").value;
    
    var myDiv = document.getElementById("myDiv");
    
    if (bgColor) {
        myDiv.style.backgroundColor = bgColor;
    }
    
    if (width) {
        myDiv.style.width = width + "px";
    }
    
    if (height) {
        myDiv.style.height = height + "px";
    }
}