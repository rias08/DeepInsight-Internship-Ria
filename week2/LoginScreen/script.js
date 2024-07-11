function welcomeMessage() {
    var username = document.getElementById("User").value;
    var password = document.getElementById("Password").value;
  
    if (username === "" || password === "") {
      console.log("Please enter both username and password.");}}