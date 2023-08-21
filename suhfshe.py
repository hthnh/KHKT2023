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
    def load_table(self):
        Window.size = (901,600)
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint = {"center_x": .5, "center_y": .5},
            rows_num = 7,
            size_hint=(0.9, 0.9),
            column_data = [
                (str(today), dp(20)),
                ("Breakfast", dp(30)),
                ("Lunch", dp(30)),
                ("Dinner", dp(30))
                ],
            row_data = [
                ("Monday", B[0], L[0],D[0]),
                ("Tuesday", B[1], L[1],D[1]),
                ("Wednesday", B[2], L[2], D[2]),
                ("Thursday", B[3], L[3],D[3]),
                ("Friday", B[4], L[4],D[4]),
                ("Saturday", B[5], L[5],D[5]),
                ("Sunday", B[6], L[6],D[6])
                ])
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()
MyApp().run()