let circle = document.getElementById("circle");
let color_input = document.getElementById("color");

color_input.addEventListener('change', () => {
    circle.style.background = color_input.value;
});