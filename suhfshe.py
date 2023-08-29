from kivy.config import Config
Config.set('graphics', 'resizable', False)

import kivy
kivy.require('1.7.0')

from kivymd.app import MDApp

from kivy.lang import Builder
Builder.load_file('TheMenu.kv')

from kivy.uix.screenmanager import Screen, ScreenManager

from kivymd.uix.datatables import MDDataTable

from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivy.uix.button import Button

from kivy.uix.checkbox import CheckBox

from kivy.uix.textinput import TextInput

from kivy.uix.dropdown import DropDown

from kivy.metrics import dp

from datetime import date
today = date.today()

import time

from kivy.core.window import Window


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
sm = ScreenManager()



class MyApp(MDApp):
    def build(self):
        sm.add_widget(MainScreen(name = "main"))
        sm.add_widget(UserScreen(name = "user"))
        sm.add_widget(FoodScreen(name = "food"))
        sm.add_widget(MenuScreen(name = "menu"))
        return sm

class UserScreen(Screen):
    def load_size(self):
        Window.size = (600,901)
    def back_screen(a, b):
        sm.current ='main'
    
    def main(self):
        input_layout = BoxLayout(orientation = 'horizontal')
        left_side = BoxLayout(orientation = "vertical")
        right_side = BoxLayout(orientation = "vertical")
        left_side.add_widget(Label(text = "GENDER INENTIFY",bold = True, color = (37/255, 64/255, 98/255, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "AGE",bold = True, color = (37/255, 64/255, 98/255, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "WEIGHT",bold = True, color = (37/255, 64/255, 98/255, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "HEIGHT",bold = True, color = (37/255, 64/255, 98/255, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "CURRENT STATUS",bold = True, color = (37/255, 64/255, 98/255, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "TYPE OF MENU",bold = True, color = (37/255, 64/255, 98/255, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))



        global sex
        sex = int(5)
        global style
        style = int(6)
        global type
        type = int(7)

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

        Male = BoxLayout(orientation = "horizontal")
        Male.add_widget(male)
        Male.add_widget(Label(text = "MALE"))
        Female = BoxLayout(orientation = "horizontal")
        Female.add_widget(female)
        Female.add_widget(Label(text = "FEMALE"))
        Sex = BoxLayout(orientation= "horizontal")
        Sex.add_widget(Male)
        Sex.add_widget(Female)

        global height
        height = TextInput(multiline=False, text = "cm")
        global weight
        weight = TextInput(multiline=False, text = "kg")
        global age
        age = TextInput(multiline=False, text = "age")


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
        def HelpStyle(event):
            layout = BoxLayout(orientation = "vertical")
            layout.add_widget(Label(text = "Office work is  work normally carried out in an office or school ") )
            layout.add_widget(Label(text = "Outdoor work is do something happens outdoors"))
            layout.add_widget(Label(text = "Exercise sometimes is sometime do physical activities to make your body strong and health"))
            layout.add_widget(Label(text = "Always exercise is always do physical activities to make your body strong and health"))
            layout.add_widget(Label(text = "Athlete is you are athlete"))
            helpPopUp = Popup(title = "Help",content = layout, auto_dismiss = True, size_hint = (0.65,0.5))
            helpPopUp.open()
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
        helpStyle = Button(text = "Help", size_hint_y = None, height = 35, on_release= lambda style: HelpStyle(event = open))
        Style.add_widget(helpStyle)
        btnStyle = Button(text = "Choice your life style")
        btnStyle.bind(on_release = Style.open)
        Style.bind(on_select = lambda instance, x: setattr(btnStyle, 'text', x))


        def takeType(value):
            global type
            if value == "Gain Weight" :
                type = 1
            elif value == "Loss Weight" :
                type = 2
            elif value == "Normal" :
                type = 3
        
        def HelpType(event):
            layout = BoxLayout(orientation = "vertical")
            layout.add_widget(Label(text = "Works well in single-user menu") )
            layout.add_widget(Label(text = "If making a menu for family, choose normal"))
            helpPopUp = Popup(title = "Help",content = layout, auto_dismiss = True, size_hint = (0.4,0.2))
            helpPopUp.open()

        typeMenu = DropDown()
        #gain weight/loss weight/normal
        Gw = Button(text = "Gain Weight",size_hint_y = None, height = 35, on_release = lambda type: takeType(value = type.text))
        Gw.bind(on_release = lambda Gw: typeMenu.select(Gw.text))
        Lw = Button(text = "Loss Weight",size_hint_y = None, height = 35, on_release = lambda type: takeType(value = type.text))
        Lw.bind(on_release = lambda Lw: typeMenu.select(Lw.text))
        Nw = Button(text = "Normal",size_hint_y = None, height = 35, on_release = lambda type: takeType(value = type.text))
        Nw.bind(on_release = lambda Nw: typeMenu.select(Nw.text))
        Help = Button(text = "Help",size_hint_y = None, height = 35, on_release = lambda type: HelpType(event=open))

        typeMenu.add_widget(Gw)
        typeMenu.add_widget(Nw)
        typeMenu.add_widget(Lw)
        typeMenu.add_widget(Help)
        btnType = Button(text = "Choice type of menu")
        btnType.bind(on_release = typeMenu.open)
        typeMenu.bind(on_select = lambda instance, x: setattr(btnType, "text", x))

        def check_add_user(self):
            if type == 1 or type == 2 or type == 3:
                if sex == 1 or sex == 0 :
                    if style == 1 or style == 2 or style == 3 or style == 4 or style == 5 :
                        if not "cm" in height.text :
                            if not "kg" in weight.text :
                                if not "age" in age.text :
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
            else :
                noti = Popup(title = "notification",content = Label(text = "Missing Type"), auto_dismiss = True, size_hint = (0.2,0.2))
                noti.open()

        def AddUser():
            with open("Core\InOut\heightWeight.txt","w") as f:
                f.write(str(sex))
                f.write("\n")
                f.write(height.text)
                f.write("\n")
                f.write(weight.text)
                f.write("\n")
                f.write(age.text)
                f.write("\n")
                f.write(str(style))
                f.write("\n")
                f.write(str(type))
            f.close()
            os.chdir("Core")
            os.system("Calories-Calculator.exe")
            os.chdir("..")
            noti = Popup(title = "notification",content = Label(text = "Add successful"), auto_dismiss = True, size_hint = (0.2,0.2))
            noti.open()

        def RemoveUser(self):
            noti = Popup(title = "notification",content = Label(text = "Remove successful"), auto_dismiss = True, size_hint = (0.2,0.2))
            noti.open()
            os.chdir("Core")
            os.system("clearTotalCalories.exe")
            os.chdir("..")
        

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

        right_side.add_widget(Sex)
        right_side.add_widget(age)
        right_side.add_widget(weight)
        right_side.add_widget(height)
        right_side.add_widget(btnStyle)
        right_side.add_widget(btnType)



        input_layout.add_widget(left_side)
        input_layout.add_widget(right_side)
        screen = BoxLayout(orientation = "vertical")
        screen.add_widget(Label(text = "ADD MEMBER", color = (37/255, 64/255, 98/255, 1), font_size = 55, bold = True))
        screen.add_widget(input_layout)
        screen.add_widget(Button(on_press = self.back_screen,size_hint = (.8, .1),pos_hint = {'center_x':.5}, text = "Back",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= ''))
        self.add_widget(screen)
        return screen
    def on_enter(self):
        self.load_size()
        self.main()
    pass
class FoodScreen(Screen):
    def load_size(self):
        Window.size = (600,901)
    def on_enter(self):
        self.load_size()
class MainScreen(Screen):
    def load_size(self):
        Window.size = (600,901)
    def on_enter(self):
        self.load_size()
    def picknow_button_on(self):
        self.ids.image_picknow.source = "Core/image/UI/ChooseIcon/PickNowChoose.png"
    def picknow_button_release(self):
        self.ids.image_picknow.source = "Core/image/UI/ButtonOfUI/ButtonPickNow.png"
    def nutrients_button_on(self):
        self.ids.image_nutrients.source = "Core/image/UI/ChooseIcon/NutriChoose.png"
    def nutrients_button_release(self):
        self.ids.image_nutrients.source = "Core/image/UI/ButtonOfUI/ButtonNutrients.png"
    def addfood_button_on(self):
        self.ids.image_addfood.source = "Core/image/UI/ChooseIcon/AddFoodchoose.png"
    def addfood_button_release(self):
        self.ids.image_addfood.source = "Core/image/UI/ButtonOfUI/ButtonAddFood.png"
    def addfamily_button_on(self):
        self.ids.image_addfamily.source = "Core/image/UI/ChooseIcon/AddFamilychoose.png"
        sm.current = "user"
    def addfamily_button_release(self):
        self.ids.image_addfamily.source = "Core/image/UI/ButtonOfUI/ButtonAddFamily.png"
    def menu_button_on(self):
        self.ids.image_menu.source = "Core/image/UI/ChooseIcon/Menuchoose.png"
        sm.current = 'menu'
    def menu_button_release(self):
        self.ids.image_menu.source = "Core/image/UI/ButtonOfUI/ButtonMenu.png"
    def order_button_on(self):
        self.ids.image_order.source = "Core/image/UI/ChooseIcon/OrderChoose.png"
    def order_button_release(self):
        self.ids.image_order.source = "Core/image/UI/ButtonOfUI/ButtonOrder.png"
    pass    


class MenuScreen(Screen):
    def load_table(self):
        Window.size = (901,600)
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint = {"center_x": .5, "center_y": .55},
            rows_num = 7,
            size_hint=(0.9, 0.8),
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