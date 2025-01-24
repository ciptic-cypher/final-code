let background = document.getElementById("background");
let text = document.getElementById("text");

function changecolor(color) {
    background.style.backgroundColor = color;
    text.textContent = color;
}