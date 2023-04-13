from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable

class MyApp(MDApp):
    def build(self):
        layout = Screen()
        layout = BoxLayout(orientation='vertical')
        table = MDDataTable(column_data=[
            ("Breakfast", dp(30)),
            ("Lunch", dp(30)),
            ("Dinner", dp(30))
        ])
        layout.add_widget(table)
        return layout


MyApp().run()