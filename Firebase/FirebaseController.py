import pyrebase

config = {
    "apiKey": "AIzaSyC6ymfHP4TgFf0PHqvE7kk2NP2Ttk_llWc",
    "authDomain": "fix-reportsws.firebaseapp.com",
    "databaseURL": "https://fix-reportsws.firebaseio.com",
    "projectId": "fix-reportsws",
    "storageBucket": "fix-reportsws.appspot.com",
    "messagingSenderId": "109866457954",
    "appId": "1:109866457954:web:7c2a64d2d61917471a2a3b"
}
 
Firebase = pyrebase.initialize_app(config)