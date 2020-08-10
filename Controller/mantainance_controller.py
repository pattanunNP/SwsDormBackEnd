
from flask import Flask, request, jsonify, Blueprint,redirect
from Service.mantainance_service import mantainance

mantainance_api = Blueprint('mantainance_api', __name__)
mantainance = mantainance()

@mantainance_api.route('/api/request-mantainance', methods=["POST","GET"])
def request_matainance():
    data = request.json
    result = mantainance.request(data)
    return result
