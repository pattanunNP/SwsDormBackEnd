from flask import Flask, request,jsonify
from Util.RefCode import refCode
import requests
from PIL import Image
import base64,os
from Firebase.FirebaseController import Firebase
import config as ENV
import io

class mantainance:
    auth = Firebase.auth()
    db = Firebase.database()
    storage = Firebase.storage()
    url = 'https://notify-api.line.me/api/notify'
    token = ENV.LINETOKEN
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}


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
    def sendNotify2Admin(data):
        r = requests.post(mantainance.url, headers=mantainance.headers, data={'message': f"ชื่อ: {data['WorkInfo']['Name']} เลขห้อง:{data['WorkInfo']['RoomCode']}{data['WorkInfo']['RoomNumber']} อาการเสีย: {data['WorkInfo']['Discription']} จัดการสอบงานซ่อมได้ที่:https://liff.line.me/1654690335-zWJedOD7"})
      
        print("Msg: ",r.text, "Status: ",r.status_code)
    
    @staticmethod
    def request(data):
        user = mantainance.auth.sign_in_with_email_and_password(ENV.FIREBASE_EMAIL, ENV.FIREBASE_PASSWORD)
        ref = refCode.gennerate_refcode(data['WorkInfo']['RoomCode'], data['WorkInfo']['RoomNumber'], data['WorkInfo']['StudentId'])
        for img in data['Image']:
            re = mantainance.stringToRGB(img, ref,user)
            data.update({'Image': {'Url': re}})
        
        mantainance.sendNotify2Admin(data)
        mantainance.db.child("work").child(ref).push(data, user['idToken'])
        response = {
            
            "payload":data,
            "message": "work has requested",
            "refCode":ref
        }
        return response

    @staticmethod
    def Update(data):
        print(data)
        user = mantainance.auth.sign_in_with_email_and_password(ENV.FIREBASE_EMAIL, ENV.FIREBASE_PASSWORD)
        if data['Status'] != "":
           mantainance.db.child("work").child(data['refId']).child(data['Id']).child("WorkInfo").update({"Status": data['Status']}, user['idToken'])
        if data['Discription'] != "":
           mantainance.db.child("work").child(data['refId']).child(data['Id']).child("WorkInfo").update({"FixDetail": data['Discription']},user['idToken'])
        return "ok"

    @staticmethod
    def Delete(data):
        print(data)
        user = mantainance.auth.sign_in_with_email_and_password(ENV.FIREBASE_EMAIL, ENV.FIREBASE_PASSWORD)
        mantainance.db.child("work").child(data['refId']).child(data['Id']).remove(user['idToken'])
        return "ok"

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
        try:
            user = mantainance.auth.sign_in_with_email_and_password(userInput['email'], userInput['password'])
            if user['idToken'] != 0:
               
                respone = {
                    "value":user['localId'],
                    "error":"",
              
                 }
                return respone
        except:
            
            respone = {
                "value":"error",
                "error":"login error maybe user or password inconrrect",
              
            }
            return respone
      
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

   
