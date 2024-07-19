function switchScreen() {
  var username = document.getElementById("User").value;
  var password = document.getElementById("Password").value;

  const data = {
    User: username,
    Password: password
  };

  const searchParams = new URLSearchParams(data);
  const url = `http://localhost:5000?${searchParams.toString()}`;
  
  window.location.href = url;
}
