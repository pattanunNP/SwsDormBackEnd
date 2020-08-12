import config as ENV
import jwt
from datetime import datetime,timedelta


class AcessControl:

    @staticmethod
    def login(data):

     
        if len(data["Name"]) != 0 and len(data["StudentId"]) >= 6:

            token = jwt.encode({
                'Name': data['Name'],
                'StudentId': data['StudentId'],
                'exp': datetime.utcnow() + timedelta(minutes=5)
            }, ENV.SECERET_KEY)

            respone = {
                "user": data['Name'],
                "StudentId": data['StudentId'],
                "token": token.decode('UTF-8'),
                "expire-in": "5 min"
            }
            return respone

        elif len(data["Name"]) == 0:
            respone = {"message": "Name must not equal blank"}
            return respone

        elif len(data["Name"]) != 0 and len(data["StudentId"]) < 6:
           respone = {"message": "StudentId must be 8 or more letters"}
           return respone

    