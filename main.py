from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
import json
import requests
from DB import wrapperDB

app = Flask(__name__)
api = Api(app,
          version="1.0",
          title="Closing API",
          description="Api of MicroService Closing")

name_space = api.namespace('closing', description='closing APIs')
resource_fields = api.model('Resource', {
    'code_contract': fields.String,
    'user_name': fields.String,
})


@api.route('/closing')
class closings(Resource):
    @api.response(200, 'Success')
    def get(self):
        """Returns list of closing."""
        # result = getAllContracts()
        result = {'data': 'closing get'}
        return jsonify(result)

    @api.response(200, 'Success')
    @api.response(400, 'Validation Error')
    @api.expect(resource_fields)
    def post(self):
        """close a contract."""
        content = request.json
        code_contract = content['code_contract']
        user_name = content['user_name']
        response = wrapperDB.updateStateClose(code_contract, user_name)
        if response == -1:
            return {'error': 'wrong request'}, 400
        result = json.dumps(response),
        # changeContract(code_contract)
        return jsonify(result)


@api.route('/closing/<code>')
@api.doc(params={'code': 'contract code'})
class closingid(Resource):
    @api.response(200, 'Success')
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
