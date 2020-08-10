import config as ENV
from flask import Flask, request, jsonify, Blueprint
from Controller.mantainance_controller import mantainance_api
from flask_cors import CORS
app = Flask(__name__, instance_relative_config=False)
app.config['JSON_SORT_KEYS'] = False
cors = CORS(app, supports_credentials=True,
            resources={r"/*": {"origins": "*"}})

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/')
def index():
    
    return jsonify({"message": "ok"})

app.register_blueprint(mantainance_api)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)