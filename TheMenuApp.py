from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import subprocess


class MenuApp(MDApp):
    def build(self):
        screen = Screen()
        mainProgram = BoxLayout(orientation = "horizontal")
        AllFunc = BoxLayout(orientation = "vertical",padding = 50)
        
        
        
        table = MDDataTable(
            pos_hint = {"center_x": .5, "center_y": .5},
            size_hint = (1, 1),
            rows_num = 7,
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



        btnAddUser = Button(text = "Add Family Member",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        btnAddUser.bind(on_press = self.AddUser)
        btnAddFood = Button(text = "Add Food",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        btnAddFood.bind(on_press = self.test)

        btnOrder = Button(text = "Order",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        btnOrder.bind(on_press = self.test)

        btnPickNow = Button(text = "Pick Now",
                            color = (0,0,0,1.000),
                            background_color =(0,249,255,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        btnPickNow.bind(on_press = self.test)

        btnNutrition = Button(text = "Nutrition",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        btnNutrition.bind(on_press = self.test)

        AllFunc.add_widget(btnAddUser)
        AllFunc.add_widget(btnAddFood)
        AllFunc.add_widget(btnOrder)
        AllFunc.add_widget(btnPickNow)
        AllFunc.add_widget(btnNutrition)





        mainProgram.add_widget(AllFunc)
        mainProgram.add_widget(table)
        screen.add_widget(mainProgram)

        return screen
    


    def test(self , event):
        print("test")
    def AddUser(seft , event):
        subprocess.Popen(["D:\code\KHKT-Order\Calories-Calculator\Calories-Calculator.exe"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
# lam popup cho FamilyMember ben trong co Add va Remove

MenuApp().run()