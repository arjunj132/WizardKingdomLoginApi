from flask import Flask
import os

database = {"jakkipally@gmail.com": "1"}

app = Flask(__name__)


@app.route('/<user>/<pwd>')
def index(user, pwd):
  from auth0.authentication import GetToken

  token = GetToken('wizardkingdom.us.auth0.com',
                   'nigaPP6liT7TlyHqCGlomyKLh03Kaiae',
                   client_secret=os.environ['secret'])

  token.login(username=user,
              password=pwd,
              realm='Username-Password-Authentication')

  return database["jakkipally@gmail.com"]


app.run(host='0.0.0.0', port=81)
