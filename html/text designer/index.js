const text = document.getElementById("text");
const input = document.getElementById("input");
const secondInput = document.getElementById("input2");
const thirdInput = document.getElementById("input3");

input.addEventListener("input", () => {
    text.style.color = input.value;
    text.style.textShadow = input.value;
    text.style.textAlign = input.value;
})

secondInput.addEventListener("input", () => {
    if (secondInput.value === "") {
        text.textContent = "Text";
        text.style.fontFamily = "Arial, Helvetica, sans-serif";
    }

    text.textContent = secondInput.value;
})

thirdInput.addEventListener("input", () => {
    if (thirdInput.value === "") {
        text.style.fontFamily = "Arial, Helvetica, sans-serif";
    }

    text.style.fontFamily = thirdInput.value;
})