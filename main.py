import json

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource
import requests
from DB import wrapperDB

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app,
          version="1.0",
          title="Closing API",
          description="Api of MicroService Closing")

name_space = api.namespace('closing', description='closing APIs')


@api.route('/closing')
class closings(Resource):
    def get(self):
        """Returns list of closing."""
        # result = getAllContracts()
        result = {'data': 'closing get'}
        return jsonify(result)

    def post(self):
        """close a contract."""
        content = request.json
        code_contract = content['code_contract']
        user_name = content['user_name']
        response = wrapperDB.updateStateClose(code_contract, user_name)
        if response == -1:
            return {'error': 'wrong request'}, 503
        result = json.dumps(response),
        # changeContract(code_contract)
        return jsonify(result)


@api.route('/closing/<code>')
class closingid(Resource):
    def get(self, code):
        """Returns a closing."""
        # result = getContractByCode(code)
        result = {'data': 'code ' + code}
        return jsonify(result)


def changeContract(code):
    response = requests.put('http://127.0.0.1:8091/api/v1/deals/close/' + code, data={'code': code})
    return response.status_code


if __name__ == '__main__':
    wrapperDB.initDB()
    app.run(port='8093')
