import kivy
kivy.require('1.7.0')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
Builder.load_file('TheMenu.kv')

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = "main"))
        sm.add_widget(UserScreen(name = "user"))
        sm.add_widget(FoodScreen(name = "food"))
        return sm

class UserScreen(Screen):
    pass
class FoodScreen(Screen):
    pass
class MainScreen(Screen):
    pass


MyApp().run()