let box = document.getElementById('box');
let input = document.getElementById('input')

input.addEventListener("input", () => {
    box.style.borderRadius = input.value;
    box.style.background = input.value;
    box.style.boxShadow = input.value;
});