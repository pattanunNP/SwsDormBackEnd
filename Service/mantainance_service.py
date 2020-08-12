from flask import Flask, request
from Util.RefCode import refCode
from Firebase.FirebaseController import Firebase
import config as ENV

class mantainance:
    db = Firebase.database()

    @staticmethod
    def request(data):
        ref = refCode.gennerate_refcode(data['WorkInfo']['RoomCode'],data['WorkInfo']['RoomNumber'],data['WorkInfo']['StudentId'])
        mantainance.db.child("work").child(ref).push(data)
        
        

        response = {
            "payload":data,
            "message": "work has requested",
            "refCode":ref
        }
        return response

    @staticmethod
    def track(refcode):
        lists = []
       
        try:
            track_data = mantainance.db.child("work").child(refcode).get()
            for data in track_data.each():
                lists.append(data.val())
        except:
            pass
    
            
        return lists
        
    @staticmethod
    def admin(refcode):
        lists = []
       
        try:
            track_data = mantainance.db.child("work").get()
            for data in track_data.each():
                lists.append(data.val())
        except:
            pass
    
            
        return lists
    
