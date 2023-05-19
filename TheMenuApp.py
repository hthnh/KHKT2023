from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label



class MenuApp(MDApp):
    def build(self):
        screen = Screen()
        mainProgram = BoxLayout(orientation = "horizontal")
        AllFunc = BoxLayout(orientation = "vertical",)
        
        
        
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



        btnAddUser = Button(text = "AddUser",
                            background_color =(0,249,255,1.000),
                            size_hint = (.5,None),
                            pos_hint = {"center_x": .5})
        btnAddUser.bind(on_press = self.test)

        btnOrder = Button(text = "Order",
                            background_color =(0,249,255,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        btnOrder.bind(on_press = self.test)

        btnPickNow = Button(text = "Pick Now",
                            background_color =(0,249,255,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        btnPickNow.bind(on_press = self.test)

        btnNutrition = Button(text = "Nutrition",
                            background_color =(0,249,255,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        btnNutrition.bind(on_press = self.test)

        AllFunc.add_widget(btnAddUser)
        AllFunc.add_widget(btnOrder)
        AllFunc.add_widget(btnPickNow)
        AllFunc.add_widget(btnNutrition)





        mainProgram.add_widget(AllFunc)
        mainProgram.add_widget(table)
        screen.add_widget(mainProgram)

        return screen
    


    def test(self , event):
        print("test")
 


MenuApp().run()