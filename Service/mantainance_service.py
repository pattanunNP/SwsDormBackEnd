from flask import Flask, request,jsonify
from Util.RefCode import refCode

from PIL import Image
import base64,os
from Firebase.FirebaseController import Firebase
import config as ENV
import io

class mantainance:
    auth = Firebase.auth()
    db = Firebase.database()
    storage = Firebase.storage()

    @staticmethod
    def stringToRGB(base64_string,ref,user):
        filename =  str(base64_string).split(',')[0]
        base64_string = str(base64_string).split(',')[2][0:-2]
       
        imgdata = base64.b64decode(base64_string)
        with open(f'./image/{filename[13:-2]}.png', 'wb') as f:
            f.write(imgdata)
        mantainance.storage.child(f"{ref}/{filename[13:-2]}.png").put(f'./image/{filename[13:-2]}.png')
        return mantainance.storage.child(f"{ref}/{filename[13:-2]}.png").get_url(user['idToken'])

        
    
    @staticmethod
    def request(data):
        user = mantainance.auth.sign_in_with_email_and_password(ENV.FIREBASE_EMAIL, ENV.FIREBASE_PASSWORD)
        ref = refCode.gennerate_refcode(data['WorkInfo']['RoomCode'], data['WorkInfo']['RoomNumber'], data['WorkInfo']['StudentId'])
        for img in data['Image']:
            re = mantainance.stringToRGB(img, ref,user)
            data.update({'Image': {'Url': re}})
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
    def login(userInput):
        user = mantainance.auth.sign_in_with_email_and_password(userInput['email'], userInput['password'])
      
        if user['idToken'] != 0:
            respone = user['localId']
            return respone
        else:
            return jsonify({"message":"error"}),400


    
    @staticmethod
    def allwork():
        lists = []
        try:
            track_data = mantainance.db.child("work").get()
            for data in track_data.each():
                lists.append(data.val())
            # print(lists)
            
        except:
            pass

        return lists
