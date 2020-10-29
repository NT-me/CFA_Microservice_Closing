from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_restful.reqparse import Namespace
import requests

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)


@app.route('/closing', methods=['GET'])
def closingsAll():
    result = {'data': 'closing post'}
    return jsonify(result)


@app.route('/closing', methods=['POST'])
def closingsAdd():
    content = request.json
    code_contract = content['code_contract']
    user_name = content['user_name']
    result = {'id': code_contract, 'status': user_name}
    changeContract(code_contract)
    return jsonify(result)


@app.route('/closing/<int:id>', methods=['GET'])
def closingid(id):
    result = {'data': 'id ' + str(id)}
    return jsonify(result)


def changeContract(code):
    response = requests.put('http://127.0.0.1:5000/api/v1/deals/close/' + str(code), data={'code': code})


if __name__ == '__main__':
    app.run(port='5000')
