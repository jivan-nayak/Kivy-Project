from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch Service Account Key Contents
cred = credentials.Certificate("serviceAccountKey.json")

# Initialise the app with service account and grating the admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'Put the firebase link here'
})

database = db.reference('py/')


class HomeWindow(Screen):
    def home(self):
        print("Home Screen")


class LoginWindow(Screen):
    usr_ref = ObjectProperty(None)
    pwd_ref = ObjectProperty(None)

    def login(self):
        ref = db.reference('py/')
        username = self.usr_ref.text
        password = self.pwd_ref.text
        users_ref = ref.child('users').child(username).get()
        if users_ref is None:
            self.usr_ref.text = ''
            self.pwd_ref.text = ''
        elif users_ref['Password'] != password:
            self.usr_ref.text = ''
            self.pwd_ref.text = ''
        else:
            self.manager.current = 'dashboard'


class SignupWindow(Screen):
    name_ref = ObjectProperty(None)
    age_ref = ObjectProperty(None)
    usr_ref = ObjectProperty(None)
    pwd_ref = ObjectProperty(None)

    def signup(self):
        ref = db.reference('py/')
        username = self.usr_ref.text
        password = self.pwd_ref.text
        name = self.name_ref.text
        age = self.age_ref.text
        users_ref = ref.child('users').child(username)
        if users_ref.get() is None:
            users_ref.set({
                "Password": password,
                "Name": name,
                "Age": age
            })


class DashBoardWindow(Screen):
    def dash(self):
        ref = db.reference('py/')
        users_ref = ref.child('cooks')
        cooks = users_ref.get()


class CookWindow(Screen):
    def cook(self):
        print("Login Screen")


class CateringServicesWindow(Screen):
    def catering(self):
        print("Login Screen")


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()