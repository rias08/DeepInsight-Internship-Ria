from flask import Flask, request, redirect, url_for;

app = Flask(__name__)

@app.route("/")
def welcomeScreen():
    User = request.args.get('User')
    Password = request.args.get('Password')
    return f"Hello {User}! Welcome to my WebApp. Your password is: {Password}"


if __name__ == "__main__":
   app.run()
    
