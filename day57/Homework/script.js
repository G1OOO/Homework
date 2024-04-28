function changeWidth() {
    var privilege = document.getElementById("privilege").value;
    var color = document.getElementById("color").value;
    var second = document.getElementById("second").value;
    var width = document.getElementById("width").value;
    var third = document.getElementById("third").value;
    var height = document.getElementById("height").value;
    var fourth = document.getElementById("fourth").value;
    var text = document.getElementById("text").value;

    var infoDiv = document.getElementById("infoDiv");
    var paragraph = infoDiv.querySelector("p");

    paragraph.innerText = text;
    infoDiv.style.width = width + "px";
  }