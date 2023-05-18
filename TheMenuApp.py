from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.button import Button


class MenuApp(MDApp):
    def build(self):
        screen = Screen()

        table = MDDataTable(
            column_data = [
                ("date", dp(20)),
                ("Breakfast", dp(30)),
                ("Lunch", dp(30)),
                ("Dinner", dp(30)),
            ],
            row_data = [
                ("Monday", "", "",""),
                ("Tuesday", "", "",""),
                ("Wednesday", "", "",""),
                ("Thursday", "", "",""),
                ("Friday", "", "",""),
                ("Saturday", "", "",""),
                ("Sunday", "", "",""),
            ]
        )

        btnAddUser = Button(text = "Add User")
        btnOrder = Button(text = "Order")
        btnPickNow = Button(text = "Pick Now")
        btnNutrition = Button(text = "Nutrition")

        

        screen.add_widget(table)

        return screen
    


MenuApp().run()