
from flask import Flask, request, jsonify, Blueprint,redirect
from Service.mantainance_service import mantainance
from Auth.CheckToken import checkToken
from Auth.Auth_Token_Service import AcessControl
mantainance_api = Blueprint('mantainance_api', __name__)
mantainance = mantainance()



@mantainance_api.route('/api/authentication', methods=["POST"])
def login():
    data = request.json
    respone = AcessControl.login(data)
    return respone

@mantainance_api.route('/api/track/', methods=["GET"])
def track():
    refcode = request.args.get('id')
    respone = mantainance.track(refcode)
    return jsonify({"works": respone})

@mantainance_api.route('/api/login', methods=["POST"])
def admin():
    userInput = request.json
    respone = mantainance.login(userInput)
    return respone

@mantainance_api.route('/api/get-allwork')
def getallwork():
    respone = mantainance.allwork()
    return jsonify({"works": respone})



@mantainance_api.route('/api/request-mantainance', methods=["POST", "GET"])
@checkToken
def request_matainance():
    data = request.json
    result = mantainance.request(data)
    return result
