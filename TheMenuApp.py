from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import subprocess
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown

class MenuApp(MDApp):
    def build(self):
        screen = Screen()
        mainProgram = BoxLayout(orientation = "horizontal")
        AllFunc = BoxLayout(orientation = "vertical",padding = 40, spacing = 20)
        
        
        
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
        btnAddUser.bind(on_press = self.User)

        btnAddFood = Button(text = "Add Food",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        btnAddFood.bind(on_press = self.Food)

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
    

    def test(self, event):
            print("test")




    def User(self , event):
        layout = BoxLayout(orientation = "vertical")
        func = BoxLayout(orientation = "horizontal", padding = 10,size_hint = (1,0.6))
        input = GridLayout(cols = 2)

        btnAdd = Button(text = "Add Member",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            pos_hint = {"center_y": .5})
        btnAdd.bind(on_press = self.AddUser)
        btnRem = Button(text = "Remove All Member",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            pos_hint = {"center_y": .5})
        btnRem.bind(on_press = self.RemoveUser)
        



        Sex = BoxLayout(orientation = "horizontal")

        def checkbox_male(checkbox, value):
            if value :
                global sex
                sex = "0"
        male = CheckBox(color = (0,0,0,1), group = "sex")
        male.bind(active = checkbox_male)

        def checkbox_female(checkbox, value):
            if value :
                global sex
                sex = "1"
        female = CheckBox(color = (0,0,0,1), group = "sex")
        female.bind(active= checkbox_female)

        Sex.add_widget(Label(text ="Male",color = (0,0,0,1)))
        Sex.add_widget(male)
        Sex.add_widget(Label(text ="Female",color = (0,0,0,1)))
        Sex.add_widget(female)

        global height
        height = TextInput(multiline=False)
        global weight
        weight = TextInput(multiline=False)
        global age
        age = TextInput(multiline=False)


        def takeStyle(value):
            global style
            if value == "office work" :
                style = "1"
            elif value == "outdoor work" :
                style = "2"
            elif value == "exercise sometimes" :
                style = "3"
            elif value == "always exercise" :
                style = "4"
            elif value == "athlete" :
                style = "5"
        Style = DropDown()
        one = Button(text = "office work", size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        one.bind(on_release = lambda one: Style.select(one.text))
        Style.add_widget(one)
        two = Button(text = "outdoor work", size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        two.bind(on_release = lambda two: Style.select(two.text))
        Style.add_widget(two)
        three = Button(text = "exercise sometimes", size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        three.bind(on_release = lambda three: Style.select(three.text))
        Style.add_widget(three)
        four = Button(text = "always exercise", size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        four.bind(on_release = lambda four: Style.select(four.text))
        Style.add_widget(four)
        five = Button(text = "athlete", size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        five.bind(on_release = lambda five: Style.select(five.text))
        Style.add_widget(five)
        btnStyle = Button(text = "Choice your life style")
        btnStyle.bind(on_release = Style.open)
        Style.bind(on_select = lambda instance, x: setattr(btnStyle, 'text', x))



        input.add_widget(Label(text = "What is your sex",color = (0,0,0,1)))
        input.add_widget(Sex)
        input.add_widget(Label(text = "Height(cm)",color = (0,0,0,1)))
        input.add_widget(height)
        input.add_widget(Label(text = "Weight(kg)",color = (0,0,0,1)))
        input.add_widget(weight)
        input.add_widget(Label(text = "Age",color = (0,0,0,1)))
        input.add_widget(age)
        input.add_widget(Label(text = "Style",color = (0,0,0,1)))
        input.add_widget(btnStyle)

        func.add_widget(btnAdd)
        func.add_widget(btnRem)


        layout.add_widget(input)
        layout.add_widget(func)
        popUp = Popup(  content  = layout,
                        auto_dismiss = True,
                        size_hint = (.8 , .8),
                        pos_hint = {"center_x": .5, "center_y": .5},
                        background_color = (255,255,255,0.8),
                        title = "Manage member",
                        title_color = (0,0,0,1.00),
                        title_align = "center",
                        title_size = dp(20))
        popUp.open()
    


    def AddUser(self, event):
        with open("D:\code\KHKT-Order\InOut\heightWeight.txt","w") as f:
            f.write(sex)
            f.write("\n")
            f.write(height.text)
            f.write("\n")
            f.write(weight.text)
            f.write("\n")
            f.write(age.text)
            f.write("\n")
            f.write(style)
        f.close()
        noti = Popup(title = "notification",content = Label(text = "Add successful"), auto_dismiss = True, size_hint = (0.2,0.2))
        noti.open()
        subprocess.Popen(["D:\code\KHKT-Order\Calories-Calculator\Calories-Calculator.exe"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()

    def RemoveUser(self, event):
        noti = Popup(title = "notification",content = Label(text = "Remove successful"), auto_dismiss = True, size_hint = (0.2,0.2))
        noti.open()
        subprocess.Popen(["D:\code\KHKT-Order\clearTotalCalories\clearTotalCalories.exe"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
    



    def Food(self, event):
        layout = BoxLayout(orientation = "vertical")
        func = BoxLayout(orientation = "horizontal", padding = 10, size_hint = (1,0.6))
        input = GridLayout(cols = 2)

        btnAdd = Button(text = "Add Food",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            pos_hint = {"center_y": .5})
        btnAdd.bind(on_press = self.add_food)
        btnRem = Button(text = "All Food",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            pos_hint = {"center_y": .5})
        #btnRem.bind(on_press = self.RemoveUser)
        func.add_widget(btnAdd)
        func.add_widget(btnRem)

        global name_food
        name_food = TextInput(multiline = False)
        global calories_of_food
        calories_of_food = TextInput(multiline = False)


        input.add_widget(Label(text = "Name food:",color = (0,0,0,1)))
        input.add_widget(name_food)
        input.add_widget(Label(text = "Calories of food:", color = (0,0,0,1)))
        input.add_widget(calories_of_food)

        layout.add_widget(input)
        layout.add_widget(func)
        popUp = Popup(  content  = layout,
                        auto_dismiss = True,
                        size_hint = (.8 , .8),
                        pos_hint = {"center_x": .5, "center_y": .5},
                        background_color = (255,255,255,0.8),
                        title = "AddFood",
                        title_color = (0,0,0,1.00),
                        title_align = "center",
                        title_size = dp(20))
        popUp.open()

    def add_food(self,event):
        print(name_food)
        print(calories_of_food)
        with open("D:\code\KHKT-Order\InOut\AllFood.txt","a") as f:
            f.write("")
            f.write("\n")
            f.write(name_food.text)
            f.write("\n")
            f.write("")
            f.write("\n")
            f.write("")
            f.write("\n")
            f.write(calories_of_food.text)
        f.close()
    



    
MenuApp().run()