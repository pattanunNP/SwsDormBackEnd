from flask import Flask, request
from Firebase.FirebaseController import Firebase
import config as ENV

class mantainance:
    db = Firebase.database()
    @staticmethod
    def request(data):
        mantainance.db.child("work").push(data)
        
        response = {
            "message":"ok"
        }
        return response

        
    