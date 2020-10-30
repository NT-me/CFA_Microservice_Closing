from flask import Flask
from DB import wrapperDB
from apis import closing

wrapperDB.initDB()

app = Flask(__name__)
app.config["DEBUG"] = True
closing.api.init_app(app)
app.run(host='127.0.0.1', port='8093')
