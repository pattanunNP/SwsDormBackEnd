from functools import wraps
import config as ENV
import jwt
from flask import Flask, request, jsonify, Blueprint

"""
There are lines for checking token from user 
"""


def checkToken(func):
    @wraps(func)
    def wrapped(*args, **kwargs):

        token = request.args.get('token', type=str)
        if not token:

            return jsonify({'message': 'Missing token!'}), 403

        jwt_options = {'verify_signature': False, 'verify_exp': True,
                       'verify_nbf': False, 'verify_iat': True, 'verify_aud': False}
        try:
            jwt.decode(token, ENV.SECERET_KEY, algorithms=[
                              'HS256'], options=jwt_options)
        except:
            return jsonify({'message': 'Invalid Token!'}), 403

        return func(*args, **kwargs)

    return wrapped

