const display = document.getElementById("display");

function appendToDisplay(input){
    display.value += input;
}

const clear = document.getElementById("clear")

function clearDisplay(){
    display.value = "";
    clear.textContent = "C";
}

function calculate(){
    try{
        display.value = eval(display.value);
    }
    catch(error){
        display.value = "Error";
    }
}