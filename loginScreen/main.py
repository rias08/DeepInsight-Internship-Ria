from flask import Flask, request

app = Flask(__name__)

listOfPeople = {

    'User1': '1234567',
    'User2': 'MyPassword',
    'User3': 'Pass3',
    'me': 'myPass'
}

@app.route("/")
def welcomeScreen():
    username = request.args.get('User')
    password = request.args.get('Password')
    print(username, password)
    if listOfPeople.get(username) == password:
        return f"Hello {username}! Welcome to my WebApp. Your password is: {password}"
    else:
        return "I'm Sorry, We couldn't find your account. Go back to try again."
    
if __name__ == "__main__":
    app.run()
