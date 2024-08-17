const form = document.getElementById("form");
const btn = document.getElementById("Enter");

function validateForm() {
  let name = form.elements.name.value;
  let email = form.elements.email.value;
  let password = form.elements.password.value;
  let message = form.elements.message.value

  if (name == "" || email == "" || password == "" || message == "") {
    alert("Incorrect, You must Enter in all fields");
    return;
  }

  alert("Message sent");
  console.log(`Name: ${name}`);
  console.log(`Email: ${email}`);
  console.log(`Password: ${password}`);
  console.log(`Message: ${message}`);
}

btn.onclick = validateForm;

let myInput = document.getElementById("password");
let letter = document.getElementById("lower-letter");
let capital = document.getElementById("upper-letter");
let number = document.getElementById("number");
let length = document.getElementById("length");

myInput.onfocus = function() {
  document.getElementById("messege").style.display = "block";
}

myInput.onblur = function() {
  document.getElementById("messege").style.display = "none";
}

myInput.onkeyup = function() {
  let lowerCaseLetters = /[a-z]/g;
  if(myInput.value.match(lowerCaseLetters)) {  
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }
  
  let upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  let numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {  
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }
  
  if(myInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
}

let background = document.getElementById("parent");
let secondBackground = document.getElementById("work");
let thirdBackground = document.getElementById("pages");
let anchor = document.querySelector(".a-anchor");
let load = document.querySelector(".loader");

function darkMode() {
  background.style.backgroundColor = "rgb(29, 29, 29)";
  background.style.color = "white";
  secondBackground.style.backgroundColor = "black";
  thirdBackground.style.backgroundColor = "rgb(29, 29, 29)";
  anchor.style.color = "white";
  load.style.borderColor = "white";
  load.style.borderTopColor = "aqua";
}