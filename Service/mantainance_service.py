from flask import Flask, request
from Util.RefCode import refCode
from PIL import Image
import base64,os
from Firebase.FirebaseController import Firebase
import config as ENV
import io

class mantainance:
    auth = Firebase.auth()
    db = Firebase.database()
   
    
    
    @staticmethod
    def request(data):
        user = mantainance.auth.sign_in_with_email_and_password(ENV.FIREBASE_EMAIL, ENV.FIREBASE_PASSWORD)
        ref = refCode.gennerate_refcode(data['WorkInfo']['RoomCode'], data['WorkInfo']['RoomNumber'], data['WorkInfo']['StudentId'])
        mantainance.db.child("work").child(ref).push(data, user['idToken'])
        response = {
            
            "payload":data,
            "message": "work has requested",
            "refCode":ref
        }
        return response

    @staticmethod
    def track(refcode):
        lists = []
        print(refcode)
        try:
            track_data = mantainance.db.child("work").child(refcode).get()
            for data in track_data.each():
                lists.append(data.val())
        except:
            pass
    
            
        return lists
        
    @staticmethod
    def admin():
        lists = []
        user = mantainance.auth.sign_in_with_email_and_password(ENV.FIREBASE_EMAIL, ENV.FIREBASE_PASSWORD)

        # try:
        #     track_data = mantainance.db.child("work").get()
        #     for data in track_data.each():
        #         lists.append(data.val())
        # except:
        #     pass
    
            
        return "lists"
    
