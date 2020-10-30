from flask import request, jsonify, Response
from flask_restplus import Api, Resource, fields
import json
import requests
from DB import wrapperDB
from aggreg import getData

api = Api(
    version="1.0",
    title="Closing API",
    description="Api of MicroService Closing"
)
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
        # result = getData.getAllContracts()
        result = json.dumps({'data': 'closing get'})
        return Response(result, status=200, mimetype='application/json')

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
        result = json.dumps(response)
        if response['change_success'] == 1:
            # respPut = changeContract(code_contract)
            return
        return jsonify(result)


@api.route('/closing/<code>')
@api.doc(params={'code': 'contract code'})
class closingid(Resource):
    @api.response(200, 'Success')
    @api.response(206, 'partial_content')
    @api.response(400, 'Contract does not exist')
    def get(self, code):
        """Returns a closing."""
        # result = getData.getContractById(code)
        result = {"status_facility": 1, "status_insurance": 1, "status_closer": 1, "contract_json": {'data': 'id' + code}}
        statusCode = 200
        if result == -1:
            return {'error': "contract don't exist"}, 400
        if result['status_facility'] == -1 or result['status_insurance'] == -1 or result['status_closer'] == -1:
            statusCode = 206
        return Response(json.dumps(result['contract_json']), status=statusCode, mimetype='application/json')


def changeContract(code):
    response = requests.put('http://127.0.0.1:8091/api/v1/deals/close/' + code, data={'code': code})
    return response.status_code