function myFunction() {
    const message = document.getElementById("p01");
    message.innerHTML = "";
    let x = document.getElementById("demo").value;
    try {
      if(x == "") {
        throw "is empty"};
      if(isNaN(x)) {
        throw "is not a number"};
      x = Number(x);
      if(x > 10) {
        throw "is too high"};
      if(x < 5) {
        throw "is too low"};
    }
    catch({err}) {
      message.innerHTML = "Error: " + err + ".";
    }
    finally  {
      document.getElementById("demo").value = "";
    }
  }

// const c = (x) => {
//     return x+2
// }   

// console.log(c(7))

// lista = [1,2,3,4,5]

// b = 1
// console.log({lista})
