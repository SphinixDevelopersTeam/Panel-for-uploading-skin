from flask import Flask
from api.db import user

test = user.User()
print(test.login('YT_TheEnderOff', '99859985ender'))

app = Flask(__name__)

if __name__ == "__main__":
	app.run(port=80)