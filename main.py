from flask import Flask
from DB import wrapperDB
from apis import closing
import os

wrapperDB.initDB()

app = Flask(__name__)
app.config["DEBUG"] = True
closing.api.init_app(app)
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
