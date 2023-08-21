import kivy
kivy.require('1.7.0')

from kivymd.app import MDApp

from kivy.lang import Builder
Builder.load_file('TheMenu.kv')

from kivy.uix.screenmanager import Screen, ScreenManager

from kivymd.uix.datatables import MDDataTable

from kivy.uix.anchorlayout import AnchorLayout

from kivy.metrics import dp

from datetime import date
today = date.today()

from kivy.config import Config
Config.set('graphics', 'resizable', '0')

from kivy.core.window import Window
Window.size = (600,901)


B = {}
L = {}
D = {}
with open("Core\InOut\DailyFood.txt","r") as f:
    for i in range(7):
        B[i] = f.readline()
    for i in range(7):
        L[i] = f.readline()
    for i in range(7):
        D[i] = f.readline()




class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = "main"))
        sm.add_widget(UserScreen(name = "user"))
        sm.add_widget(FoodScreen(name = "food"))
        sm.add_widget(MenuScreen(name = "menu"))
        return sm

class UserScreen(Screen):
    pass
class FoodScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class MenuScreen(Screen):
    pass

MyApp().run()