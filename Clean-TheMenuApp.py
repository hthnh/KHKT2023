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
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

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



        btnAddMem = Button(text = "Add Family Member",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5},
                            on_press = btnUser.family_Member)

        btnAddFood = Button(text = "Add Food",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5},
                            on_press = Food.mainPopUp)


        btnOrder = Button(text = "Order",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        # btnOrder.bind(on_press = self.test)

        btnPickNow = Button(text = "Pick Now",
                            color = (0,0,0,1.000),
                            background_color =(0,249,255,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        # btnPickNow.bind(on_press = self.test)

        btnNutrition = Button(text = "Nutrition",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            size_hint = (.5,.5),
                            pos_hint = {"center_x": .5})
        # btnNutrition.bind(on_press = self.test)
        



        AllFunc.add_widget(btnAddMem)
        AllFunc.add_widget(btnAddFood)
        AllFunc.add_widget(btnOrder)
        AllFunc.add_widget(btnPickNow)
        AllFunc.add_widget(btnNutrition)

        mainProgram.add_widget(AllFunc)
        mainProgram.add_widget(table)
        
        screen.add_widget(mainProgram)

        return screen



class btnUser():

    def family_Member(self):
        input = GridLayout(cols = 2)
        Sex = BoxLayout(orientation = "horizontal")
        global sex
        sex = int(5)
        global style
        style = int(6)

        def checkbox_male(checkbox, value):
            if value :
                global sex
                sex = 0
        male = CheckBox(color = (0,0,0,1), group = "sex")
        male.bind(active = checkbox_male)

        def checkbox_female(checkbox, value):
            if value :
                global sex
                sex = 1
        female = CheckBox(color = (0,0,0,1), group = "sex")
        female.bind(active= checkbox_female)

        Sex.add_widget(Label(text ="Male",color = (0,0,0,1)))
        Sex.add_widget(male)
        Sex.add_widget(Label(text ="Female",color = (0,0,0,1)))
        Sex.add_widget(female)

        global height
        height = TextInput(multiline=False, text = "cm")
        global weight
        weight = TextInput(multiline=False, text = "kg")
        global age
        age = TextInput(multiline=False, text = "year")


        def takeStyle(value):
            global style
            if value == "office work" :
                style = 1
            elif value == "outdoor work" :
                style = 2
            elif value == "exercise sometimes" :
                style = 3
            elif value == "always exercise" :
                style = 4
            elif value == "athlete" :
                style = 5
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
        input.add_widget(Label(text = "Height",color = (0,0,0,1)))
        input.add_widget(height)
        input.add_widget(Label(text = "Weight",color = (0,0,0,1)))
        input.add_widget(weight)
        input.add_widget(Label(text = "Age",color = (0,0,0,1)))
        input.add_widget(age)
        input.add_widget(Label(text = "Style",color = (0,0,0,1)))
        input.add_widget(btnStyle)



        def check_add_user(self):
            if sex == 1 or sex == 0 :
                if style == 1 or style == 2 or style == 3 or style == 4 or style == 5 :
                    if not "cm" in height.text :
                        if not "kg" in weight.text :
                            if not "year" in age.text :
                                AddUser()
                            else :
                                noti = Popup(title = "notification",content = Label(text = "Missing Age"), auto_dismiss = True, size_hint = (0.2,0.2))
                                noti.open()
                        else :
                            noti = Popup(title = "notification",content = Label(text = "Missing Weight"), auto_dismiss = True, size_hint = (0.2,0.2))
                            noti.open()
                    else :
                        noti = Popup(title = "notification",content = Label(text = "Missing Height"), auto_dismiss = True, size_hint = (0.2,0.2))
                        noti.open()
                else :
                    noti = Popup(title = "notification",content = Label(text = "Missing Style"), auto_dismiss = True, size_hint = (0.2,0.2))
                    noti.open()
            else :
                noti = Popup(title = "notification",content = Label(text = "Missing Sex"), auto_dismiss = True, size_hint = (0.2,0.2))
                noti.open()

        def AddUser():
            with open("D:\code\KHKT-Order\InOut\heightWeight.txt","w") as f:
                f.write(str(sex))
                f.write("\n")
                f.write(height.text)
                f.write("\n")
                f.write(weight.text)
                f.write("\n")
                f.write(age.text)
                f.write("\n")
                f.write(str(style))
            f.close()
            noti = Popup(title = "notification",content = Label(text = "Add successful"), auto_dismiss = True, size_hint = (0.2,0.2))
            noti.open()
            subprocess.Popen(["D:\code\KHKT-Order\Calories-Calculator\Calories-Calculator.exe"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()

        def RemoveUser(self):
            noti = Popup(title = "notification",content = Label(text = "Remove successful"), auto_dismiss = True, size_hint = (0.2,0.2))
            noti.open()
            subprocess.Popen(["D:\code\KHKT-Order\clearTotalCalories\clearTotalCalories.exe"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
        

        func = BoxLayout(orientation = "horizontal", padding = 10,size_hint = (1,0.6))
        btnAdd = Button(text = "Add Member",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            pos_hint = {"center_y": .5})
        btnAdd.bind(on_press = check_add_user)
        btnRem = Button(text = "Remove All Member",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            pos_hint = {"center_y": .5})
        btnRem.bind(on_press = RemoveUser)

        func.add_widget(btnAdd)
        func.add_widget(btnRem)

        
        
        layout = BoxLayout(orientation = "vertical")
        
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

        

class Food():
    def mainPopUp(self):
        func = BoxLayout(orientation = "horizontal", padding = 10, size_hint = (1,0.6))
        def add_food(self):
            with open("D:\code\KHKT-Order\InOut\AllFood.txt","a") as f:
                f.write("\n")
                f.write(" ")
                f.write("\n")
                f.write(name_food.text)
                f.write("\n")
                f.write("0")
                f.write("\n")
                f.write("0")
                f.write("\n")
                f.write(calories_of_food.text)
            f.close()
        btnAdd = Button(text = "Add Food",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            pos_hint = {"center_y": .5},
                            on_press = add_food)
        def screenAllFood(self):
            f = open("D:\code\KHKT-Order\InOut\AllFood.txt","r")
            food = f.readlines()
            food = [s.replace("\n","") for s in food]
            
            mainWindow = GridLayout(cols = 1, spacing=10, size_hint_y=None)
            mainWindow.bind(minimum_height=mainWindow.setter('height'))

            
            for i in range(2):
                foodCard = BoxLayout(orientation = "horizontal")
                icon = Image(source='D:\code\KHKT-Order\meal-food-icon.png',size_hint = (0.25,None))
                foodCard.add_widget(icon)
                mainInformation = BoxLayout(orientation = "horizontal")
                idLabel = Label(text = "id", height = 50)
                nameLabel = Label(text = "name")
                pickTimeLabel = Label(text = "pick time")
                lastPickLabel = Label(text = "last pick")
                caloriesLabel = Label(text = "calories")
                mainInformation.add_widget(idLabel)
                mainInformation.add_widget(nameLabel)
                mainInformation.add_widget(pickTimeLabel)
                mainInformation.add_widget(lastPickLabel)
                mainInformation.add_widget(caloriesLabel)
                foodCard.add_widget(mainInformation)
                btnDelete = Button(text = "Delete",font_size = dp(20),size_hint = (0.25,None))
                foodCard.add_widget(btnDelete)
                mainWindow.add_widget(foodCard)

            
            
            scroll = ScrollView(size_hint=(1, None), size = (300,300))
            scroll.add_widget(mainWindow)
            Allfood = Popup(content  = scroll,
                        auto_dismiss = True,
                        size_hint = (.8 , .8),
                        pos_hint = {"center_x": .5, "center_y": .5},
                        background_color = (255,255,255,0.8),
                        title = "All Food",
                        title_color = (0,0,0,1.00),
                        title_align = "center",
                        title_size = dp(20))
            Allfood.open()





        btnAll = Button(text = "All Food",
                            background_color =(0,249,255,1.000),
                            color = (0,0,0,1.000),
                            pos_hint = {"center_y": .5})
        btnAll.bind(on_press = screenAllFood)
        func.add_widget(btnAdd)
        func.add_widget(btnAll)

        input = GridLayout(cols = 2)
        global name_food
        name_food = TextInput(text = "name",multiline = False)
        global calories_of_food
        calories_of_food = TextInput(text = "calories",multiline = False)

        input.add_widget(Label(text = "Name food:",color = (0,0,0,1)))
        input.add_widget(name_food)
        input.add_widget(Label(text = "Calories of food:", color = (0,0,0,1)))
        input.add_widget(calories_of_food)

        layout = BoxLayout(orientation = "vertical")
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



MenuApp().run()