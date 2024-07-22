from flask import Flask, request

app = Flask(__name__)

listOfPeople = {

    'User1': '1234567',
    'User2': 'MyPassword',
    'User3': 'Pass3',
    'me': 'myPass'
}

@app.route("/")
def html():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Screen</title>
        <script type="text/javascript" src="/static/script.js"></script>
    </head>
    <body>
      <center>
        <h1>Welcome to ______!!</h1>
        <h2>Please Enter Your Login:</h2> 
        <h3> 
          <td>Username:</td>
          <td>
          <input type="text" name='User' id='User'>
          </td>
        </h3>
        <h3>
          <td>Password:</td>
          <td><input type='password' name='Password' id='Password'></td>
        </h3>
        <h3>
          <td>
            <input type='submit' id='submit' value='Login' onclick="switchScreen()">
          </td>
        </h3>
      </center>
    </body>
    </html>
    '''

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
