import json

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_swagger import swagger
import requests

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)


@app.route('/closing', methods=['GET'])
def closingsAll():
    # result = getAllContracts()
    result = {'data': 'closing get'}
    return jsonify(result)


@app.route('/closing/<int:code>', methods=['GET'])
def closingid(code):
    # result = getContractByCode(code)
    result = {'data': 'code ' + str(code)}
    return jsonify(result)


@app.route('/closing', methods=['POST'])
def closingsAdd():
    content = request.json
    code_contract = content['code_contract']
    user_name = content['user_name']
    # response = wrapperDB.updateStateClose(code_contract, user_name)
    response = {'timestamp': 3578, 'user': 2, 'change_success': 0}
    if response == -1:
        return {'error': 'wrong request'}
    result = json.dumps(response),
    # changeContract(code_contract)
    return jsonify(result)


def changeContract(code):
    response = requests.put('http://127.0.0.1:8091/api/v1/deals/close/' + str(code), data={'code': code})
    return response.status_code


if __name__ == '__main__':
    app.run(port='8093')
