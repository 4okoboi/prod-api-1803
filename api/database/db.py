import pyrebase

firebaseConfig = {'apiKey': "AIzaSyDyjavRrXVFiAAE1fHkooPzU5ESCsh_kMY",
                  'authDomain': "api-cloacking.firebaseapp.com",
                  'databaseURL': "https://api-cloacking-default-rtdb.europe-west1.firebasedatabase.app",
                  'projectId': "api-cloacking",
                  'storageBucket': "api-cloacking.appspot.com",
                  'messagingSenderId': "181358320917",
                  'appId': "1:181358320917:web:e3f8f707a3918e14f5dd1c"}

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

print(dict(database.child('urls').child('id_1').get().val()))