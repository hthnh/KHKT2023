from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

class MyApp(MDApp):
    def build(self):
        Builder.load_file("D:\code\KHKT-Order\MainProgram.kv")
        layout = Screen()
        layout = BoxLayout(orientation='horizontal')
        Allbutton = BoxLayout(orientation='vertical')
        table = MDDataTable(
            column_data=[
             ("Date",dp(30)),
             ("Breakfast",dp(30)),
             ("Lunch",dp(30)),
             ("Dinner",dp(30))
            ],
            row_data=[
             ("Monday","","",""),
             ("Tuesday","","",""),
             ("Wednesday","","",""),
             ("Thursday","","",""),
             ("Friday","","",""),
             ("Saturday","","",""),
             ("Sunday","","","")
            ]
        )
        button1 = MDRectangleFlatButton(
            text="Add User",
            pos_hint={'center_x':0.5},
            on_release=self.btnfunc
        )
        button2 = MDRectangleFlatButton(
            text="Order",
            pos_hint={'center_x':0.5},
            on_release=self.btnfunc
        )
        button3 = MDRectangleFlatButton(
            text="Pick Now",
            pos_hint={'center_x':0.5},
            on_release=self.btnreturn
        )
        button4 = MDRectangleFlatButton(
            text="Nutrition",pos_hint={'center_x':0.5},on_release=self.btnfunc)
        Allbutton.add_widget(button1)
        Allbutton.add_widget(button2)
        Allbutton.add_widget(button3)
        Allbutton.add_widget(button4)
        layout.add_widget(Allbutton)
        layout.add_widget(table)
        return layout
    def btnfunc(self,obj):
            print("button is pressed!!")
    def btnreturn(self,obj):
            print("hel")

MyApp().run()