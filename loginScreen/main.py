from flask import Flask, request, redirect, url_for;
import requests;


app = Flask(__name__)

listOfPeople = {'User1':'1234567', 'User2':'MyPassword','User.3': 'Pass.3', 'me':'myPass'}

@app.route("/")
def welcomeScreen():
    User = request.args.get('User')
    Password = request.args.get('Password')
   # return f"Username : {User}. Password : {Password}."
    for item in listOfPeople:
        if User == item and Password == item:
            return f"Hello {User}! Welcome to my WebApp. Your password is: {Password}"
        else:
            return "I'm Sorry,  We couldn't find your account. Go back to try again."
    
if __name__ == "__main__":
   app.run()

