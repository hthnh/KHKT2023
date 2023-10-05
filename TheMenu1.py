from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivymd.icon_definitions import md_icons

import kivy
kivy.require('1.7.0')

from kivymd.app import MDApp

from kivy.lang import Builder
# Builder.load_file('TheMenu.kv')
Builder.load_string("""
<MainScreen>:
    size:(600,901)
    canvas.before:
        Color:
            rgb:(27/255, 46/255, 71/255)
        Rectangle:
            pos: self.pos
            size: self.size
    
    BoxLayout:
        background_color:(0,1,0)
        orientation: "horizontal"
        RelativeLayout:
            Image:
                source: 'logo.png'
                pos_hint: {'top': 1, 'x': 0.35}
                size_hint:(.3 , .3)
            Label:
                text: 'THE MENU'
                pos_hint: {'x':0,'y':0.15}
                font_size: 80
                underline: True
                bold: True
                font_name: "Core/image/UI/Text/Bevan-Regular.ttf"
                color: (0/255, 252/255, 255/255)
            Button:
                on_press: root.picknow_button_on()
                on_release: root.picknow_button_release()
                pos_hint: {'x':.05, 'y':.4}
                size_hint:(.255,.2)
                background_color: 0, 0, 0, 0
                Image:
                    id: image_picknow
                    source:"Core/image/UI/ButtonOfUI/ButtonPickNow.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    size: self.parent.size
            Label:
                text: "Pick Now"
                pos_hint: {'x':-0.32, 'y':-0.105}
                font_size: 30
                font_name: "Core/image/UI/Text/NotoSans-Medium.ttf"
                color: (0/255, 252/255, 255/255)
            Button:
                on_press: root.nutrients_button_on()
                on_release: root.nutrients_button_release()
                pos_hint: {'x':.375, 'y':.4}
                size_hint:(.25,.2)
                background_color: 0, 0, 0, 0
                Image:
                    id: image_nutrients
                    source:"Core/image/UI/ButtonOfUI/ButtonNutrients.png"
                    center_y: self.parent.center_y
                    center_x: self.parent.center_x
                    size: self.parent.size
            Label:
                text: "Nutrients"
                pos_hint: {'x':0, 'y':-0.105}
                font_size: 30
                font_name: "Core/image/UI/Text/NotoSans-Medium.ttf"
                color: (0/255, 252/255, 255/255)
            Button:
                on_press: root.addfood_button_on()
                on_release: root.addfood_button_release()
                pos_hint: {'x':.7,'y':.4}
                size_hint:(.25,.2)
                background_color: 0, 0, 0, 0
                Image:
                    id: image_addfood
                    source:"Core/image/UI/ButtonOfUI/ButtonAddFood.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    size: self.parent.size
            Label:
                text: "Add Food"
                pos_hint: {'x':0.33, 'y':-0.105}
                font_size: 30
                font_name: "Core/image/UI/Text/NotoSans-Medium.ttf"
                color: (0/255, 252/255, 255/255)
            Button:
                on_press: root.addfamily_button_on()
                on_release: root.addfamily_button_release()
                pos_hint: {'x':.05, 'y':.15}
                size_hint:(.25,.2)
                background_color: 0, 0, 0, 0
                Image:
                    id: image_addfamily
                    source:"Core/image/UI/ButtonOfUI/ButtonAddFamily.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    size: self.parent.size
            Label:
                text: "Add Family"
                pos_hint: {'x':-0.32, 'y':-0.355}
                font_size: 30
                font_name: "Core/image/UI/Text/NotoSans-Medium.ttf"
                color: (0/255, 252/255, 255/255)
            Button:
                on_press: root.menu_button_on()
                on_release: root.menu_button_release()
                pos_hint: {'x':.375, 'y':.15}
                size_hint:(.25,.2)
                background_color: 0, 0, 0, 0
                Image:
                    id: image_menu
                    source:"Core/image/UI/ButtonOfUI/ButtonMenu.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    size: self.parent.size
            Label:
                text: "Menu"
                pos_hint: {'x':0, 'y':-0.355}
                font_size: 30
                font_name: "Core/image/UI/Text/NotoSans-Medium.ttf"
                color: (0/255, 252/255, 255/255)
            Button:
                on_press: root.order_button_on()
                on_release: root.order_button_release()
                pos_hint: {'x':.7, 'y':.15}
                size_hint:(.25,.2)
                background_color: 0, 0, 0, 0
                Image:
                    id: image_order
                    source:"Core/image/UI/ButtonOfUI/ButtonOrder.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    size: self.parent.size
            Label:
                text: "Order"
                pos_hint: {'x':0.33, 'y':-0.355}
                font_size: 30
                font_name: "Core/image/UI/Text/NotoSans-Medium.ttf"
                color: (0/255, 252/255, 255/255)
<MenuScreen>:
    size:root.size
    Button:
        on_press: root.manager.current = 'main'
        size_hint: (.8,.1)
        pos_hint: {'center_x':0.5, 'y':0.01}
        background_normal: ''
        background_color: (27/255, 46/255, 71/255)
        Label:
            text: "Back"
            font_size: 30
            center_x: self.parent.center_x
            center_y: self.parent.center_y
            


<NotiPopup@Popups>:



<UserScreen>:
    canvas.before:
        Color:
            rgb:(27/255, 46/255, 71/255)
        Line:
            width: 5
            points: self.x,self.center_y*1.8,self.center_x*2,self.center_y*1.8

<NutrientsScreen>:
    canvas.before:
        Color:
            rgb:(27/255, 46/255, 71/255)
        Line:
            width: 5
            points: self.x,self.center_y*1.8,self.center_x*2,self.center_y*1.8



<FoodScreen>:
    canvas.before:
        Color:
            rgb:(27/255, 46/255, 71/255)
        Line:
            width: 5
            points: self.x,self.center_y*1.8,self.center_x*2,self.center_y*1.8






""")

from kivy.uix.screenmanager import Screen, ScreenManager

from kivymd.uix.datatables import MDDataTable

from kivymd.uix.card import MDCard

from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivymd.uix.dropdownitem import MDDropDownItem

from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

from kivy.uix.checkbox import CheckBox

from kivy.uix.textinput import TextInput

from kivy.uix.dropdown import DropDown

from kivy.uix.image import Image

from kivy.uix.scrollview import ScrollView

from kivy.uix.popup import Popup

from kivy.uix.gridlayout import GridLayout

from kivymd.uix.gridlayout import GridLayout

from kivy.metrics import dp

from datetime import date
today = date.today()

import time

from kivy.core.window import Window

import os
from pathlib import Path

path_to = os.getcwd()
os.chdir(path_to)

path = Path(path_to +"\Core\InOut\AllFood.txt")

if path.is_file():
    os.chdir("Core\InOut")
    if os.path.getsize("TotalCalories.txt") != 0 :
        os.chdir("..")
        os.system("ActivateCore.exe")
    else:
        os.chdir("..")

    os.chdir("..")
else: 
    print(path_to)
    os.chdir("Core")
    os.system("ImportFile.exe")
    os.chdir("..")


import pyuac
if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()
    exit()


import ctypes
from screeninfo import get_monitors

size_screen_x = 600
size_screen_y = 901

# 600 901


scale = ctypes.windll.shcore.GetScaleFactorForDevice(0)/100
size_screen_x = 600 * (2-scale)
size_screen_y = 901 * (2-scale)





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





class UserScreen(Screen):
    def load_size(self):
        Window.size = (size_screen_x, size_screen_y)
    
    def main(self):
        input_layout = BoxLayout(orientation = 'horizontal')
        left_side = BoxLayout(orientation = "vertical",spacing = 20)
        right_side = BoxLayout(orientation = "vertical", spacing = 20)
        
        left_side.add_widget(Label(text = "GENDER INENTIFY",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "AGE",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "WEIGHT",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "HEIGHT",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "CURRENT STATUS",font_size = 23,bold = True, color =(0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))



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
        Male.add_widget(Label(text = "MALE",bold = True, color = (0, 0, 0, 1)))
        
        Female = BoxLayout(orientation = "horizontal")
        Female.add_widget(female)
        Female.add_widget(Label(text = "FEMALE",bold = True,color = (0, 0, 0, 1)))

        Sex = BoxLayout(orientation= "horizontal")
        Sex.add_widget(Male)
        Sex.add_widget(Female)

        global height
        height = TextInput(multiline=False, text = "cm",background_normal = "", background_color = (132/255,166/255,207/255,0.8))
        global weight
        weight = TextInput(multiline=False, text = "kg",background_normal = "", background_color = (132/255,166/255,207/255,0.8))
        global age
        age = TextInput(multiline=False, text = "age",background_normal = "", background_color = (132/255,166/255,207/255,0.8))


        def takeStyle(value):
            global style
            if value == "Office work" :
                style = 1
            elif value == "Outdoor work" :
                style = 2
            elif value == "Exercise sometimes" :
                style = 3
            elif value == "Always exercise" :
                style = 4
            elif value == "Athlete" :
                style = 5

        def HelpStyle(event):
            layout = BoxLayout(orientation = "vertical")
            l1 = Label(color = (0,0,0,1) ,text = "Office work is  work normally carried out in an office or school ")
            l1.bind(size=lambda s, w: s.setter('text_size')(s, w))
            layout.add_widget(l1)
            l2 = Label(color = (0,0,0,1) ,text = "Outdoor work is do something happens outdoors")
            l2.bind(size=lambda s,w : s.setter('text_size')(s,w))
            layout.add_widget(l2)
            l3 = Label(color = (0,0,0,1) ,text = "Exercise sometimes is sometime do physical activities to make your body strong and health")
            l3.bind(size=lambda s,w : s.setter('text_size')(s,w))
            layout.add_widget(l3)
            l4 = Label(color = (0,0,0,1) ,text = "Always exercise is always do physical activities to make your body strong and health")
            l4.bind(size=lambda s,w : s.setter('text_size')(s,w))
            layout.add_widget(l4)
            l5 = Label(color = (0,0,0,1) ,text = "Athlete is you are athlete")
            l5.bind(size=lambda s,w : s.setter('text_size')(s,w))
            layout.add_widget(l5)
            helpPopUp = Popup(title = "Help",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = layout, auto_dismiss = True, size_hint = (0.675,0.5))
            helpPopUp.open()
        
        Style = DropDown()

        one = Button(text = "Office work",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        one.bind(on_release = lambda one: Style.select(one.text))
        Style.add_widget(one)

        two = Button(text = "Outdoor work",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        two.bind(on_release = lambda two: Style.select(two.text))
        Style.add_widget(two)

        three = Button(text = "Exercise sometimes",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        three.bind(on_release = lambda three: Style.select(three.text))
        Style.add_widget(three)
        
        four = Button(text = "Always exercise",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        four.bind(on_release = lambda four: Style.select(four.text))
        Style.add_widget(four)

        five = Button(text = "Athlete",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        five.bind(on_release = lambda five: Style.select(five.text))
        Style.add_widget(five)

        helpStyle = Button(text = "Help",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: HelpStyle(event = open))
        Style.add_widget(helpStyle)

        btnStyle = Button(text = "Choice your life style",background_normal = "", background_color = (132/255,166/255,207/255,1))
        btnStyle.bind(on_release = Style.open)
        Style.bind(on_select = lambda instance, x: setattr(btnStyle, 'text', x))


        
        
       


        def check_add_user(self):
            try :
                int(age.text)
                int(height.text)
                int(weight.text)
            except:
                noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Wrong type of input",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
                noti.open()
            else:
                if (sex == 1 or sex == 0) and isinstance(sex, int) :
                    if not "age" in age.text and isinstance(int(age.text), int) :
                        if not "kg" in weight.text :
                            if not "cm" in height.text :
                                if style == 1 or style == 2 or style == 3 or style == 4 or style == 5 :
                                        AddUser()
                                else :
                                    noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Missing Style",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
                                    noti.open()
                            else :
                                noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Missing Height",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
                                noti.open()
                        else :
                            noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Missing Weight",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
                            noti.open()
                    else :
                        noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Missing Age",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
                        noti.open()
                else :
                    noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Missing Sex",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
                    noti.open()

        def AddUser():
            with open("Core\InOut\heightWeight.txt","at") as f:
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
            f.close()
            os.chdir("Core")
            os.system("Calories-Calculator.exe")
            os.chdir("..")
            noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Add successful",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
            noti.open()

        def RemoveUser(self):
            noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Remove successful",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
            noti.open()
            os.chdir("Core")
            os.system("clearTotalCalories.exe")
            os.chdir("..")
        

        func = BoxLayout(orientation = "horizontal", padding = 10,size_hint = (1,0.6))

        btnAdd = Button(text = "Add Member",background_color =(0,249,255,1.000),color = (0,0,0,1.000),pos_hint = {"center_y": .5})
        btnAdd.bind(on_press = check_add_user)

        btnRem = Button(text = "Remove All Member",background_color =(0,249,255,1.000),color = (0,0,0,1.000), pos_hint = {"center_y": .5})
        btnRem.bind(on_press = RemoveUser)

        right_side.add_widget(Sex)
        right_side.add_widget(age)
        right_side.add_widget(weight)
        right_side.add_widget(height)
        right_side.add_widget(btnStyle)


        btn_side = BoxLayout(orientation = "horizontal",spacing = 10,size_hint = (1,.3))
        btn_side.add_widget(Button(text = "ADD FAMILY MEMBER",on_release = check_add_user,font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))
        btn_side.add_widget(Button(text = "MANAGE FAMILY MEMBER",on_release = MainScreen.developing,font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))
        btn_side.add_widget(Button(text = "DELETE ALL MEMBER",on_release = RemoveUser,font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))



        input_layout.add_widget(left_side)
        input_layout.add_widget(right_side)

        screen = BoxLayout(orientation = "vertical", spacing = 15)
        screen.add_widget(Label(text = "ADD MEMBER", color = (37/255, 64/255, 98/255, 1), font_size = 30, bold = True, size_hint = (1,.2)))
        screen.add_widget(input_layout)
        screen.add_widget(btn_side)
        screen.add_widget(Button(on_press = themenu.to_MainScreen,size_hint = (.8, .1),pos_hint = {'center_x':.5}, text = "Back",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= ''))

        self.add_widget(screen)
        return screen
    def on_enter(self):
        self.load_size()
        self.main()


class FoodScreen(Screen):
    def load_size(self):
        Window.size = (size_screen_x,size_screen_y)

    def deleteAllFood(self,a):
        def delete1():
            f = open("Core\InOut\AllFood.txt","w")
            f.write("")
            f.close()
        def delete(value):
            if "yes" in value:
                delete1()
                noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Remove successful",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
                noti.open()
        layout = BoxLayout(orientation = "vertical",spacing = 10)
        layout.add_widget(Label(font_size = 15,text = "Are You Sure To Remove All Food(type 'yes' to confirm)",color = (0,0,0,1)))
        x = TextInput()
        layout.add_widget(x)
        layout.add_widget(Button(text = "Confirm",on_press = lambda y: delete(value = x.text),font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))
        layout.add_widget(Button(text = "No", on_press = lambda *args: noti.dismiss(),font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))
        noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = layout, auto_dismiss = True, size_hint = (.7,.3))
        noti.open()

    def main(self):
        input_layout = BoxLayout(orientation = 'horizontal')
        left_side = BoxLayout(orientation = "vertical",spacing = 20)
        right_side = BoxLayout(orientation = "vertical", spacing = 20)

        left_side.add_widget(Label(text = "NAME FOOD",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "CALORIES",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "Carbohydrate",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "Protein",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "Fat",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "WITH(OUT) RICE",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "TIME OF DAY",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))


        def add_food(self):
            
            os.chdir("Core")
            os.system("findIdFood.exe")
            os.chdir("..")

            f = open("Core\InOut\IDfood.txt","r")
            Id = f.readline()
            f.close()

            with open("Core\InOut\Allfood.txt","a") as f:
                f.write(str(Id))
                f.write("\n")
                f.write(name_food.text)
                f.write("\n")
                f.write(''.join(str(x) for x in TOD))
                f.write("\n")
                f.write(str(rice))
                f.write("\n")
                f.write("0")
                f.write("\n")
                f.write("0")
                f.write("\n")
                f.write(calories_of_food.text)
                f.write("\n")
                f.write(carbohydrate_of_food.text)
                f.write("\n")
                f.write(protein_of_food.text)
                f.write("\n")
                f.write(fat_of_food.text)
                f.write("\n")
           
            noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Add successful",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
            noti.open()



        

        global name_food
        name_food = TextInput(text = "name",multiline = False,background_normal = "", background_color = (132/255,166/255,207/255,0.8))
        global calories_of_food
        calories_of_food = TextInput(text = "calories",multiline = False,background_normal = "", background_color = (132/255,166/255,207/255,0.8))
        global carbohydrate_of_food
        carbohydrate_of_food = TextInput(text = "gram",multiline = False,background_normal = "", background_color = (132/255,166/255,207/255,0.8))
        global protein_of_food
        protein_of_food = TextInput(text = "gram",multiline = False,background_normal = "", background_color = (132/255,166/255,207/255,0.8))
        global fat_of_food
        fat_of_food = TextInput(text = "gram",multiline = False,background_normal = "", background_color = (132/255,166/255,207/255,0.8))


        global TOD
        TOD = [0,0,0]

        def checkbox_Morning(checkbox, value):
            global TOD
            if value :
                TOD[0] = 1
            else :
                TOD[0] = 0
        
        def checkbox_Noon(checkbox, value):
            global TOD
            if value :
                TOD[1] = 2
            else :
                TOD[1] = 0

        def checkbox_Afternoon(checkbox, value):
            global TOD
            if value :
                TOD[2] = 3
            else :
                TOD[2] = 0
        

        global rice 
        rice = int(1)

        def checkbox_WR(checkbox, value):
            if value :
                global rice
                rice = 1

        def checkbox_WOR(checkbox, value):
            if value :
                global rice
                rice = 0

        WR = CheckBox(group = 'rice',color = (37/255, 64/255, 98/255, 1))
        WR.bind(active = checkbox_WR)
        WOR = CheckBox(group = 'rice',color = (37/255, 64/255, 98/255, 1))
        WOR.bind(active = checkbox_WOR)
        withRice = BoxLayout(orientation = "horizontal")
        withRice.add_widget(Label())
        withRice.add_widget(WR)
        withRice.add_widget(Label(text = "WITH RICE",halign="left", color = (0,0,0,1)))
        withRice.add_widget(Label())

        withoutRice = BoxLayout(orientation = "horizontal")
        withoutRice.add_widget(Label())
        withoutRice.add_widget(WOR)
        withoutRice.add_widget(Label(text = "WITHOUT RICE",halign="left", color = (0,0,0,1)))
        withoutRice.add_widget(Label())
        
        RICE = BoxLayout(orientation = "vertical")
        RICE.add_widget(withRice)
        RICE.add_widget(withoutRice)

        M = CheckBox(color = (37/255, 64/255, 98/255, 1))
        M.bind(active = checkbox_Morning)

        N = CheckBox(color = (37/255, 64/255, 98/255, 1))
        N.bind(active = checkbox_Noon)

        AN = CheckBox(color = (37/255, 64/255, 98/255, 1))
        AN.bind(active = checkbox_Afternoon)

        Morning = BoxLayout(orientation = "horizontal")
        Morning.add_widget(Label())
        Morning.add_widget(M)
        Morning.add_widget(Label(text = "MORNING",halign="left", color = (0,0,0,1)))
        Morning.add_widget(Label())

        Noon = BoxLayout(orientation = "horizontal")
        Noon.add_widget(Label())
        Noon.add_widget(N)
        Noon.add_widget(Label(text = "NOON",halign = 'left',color = (0,0,0,1)))
        Noon.add_widget(Label())

        Afternoon = BoxLayout(orientation = "horizontal")
        Afternoon.add_widget(Label())
        Afternoon.add_widget(AN)
        Afternoon.add_widget(Label(text = "AFTERNOON",halign = 'left',color = (0,0,0,1)))
        Afternoon.add_widget(Label())

        TOTD = BoxLayout(orientation = "vertical")
        TOTD.add_widget(Morning)                                                           
        TOTD.add_widget(Noon)
        TOTD.add_widget(Afternoon)
        

        right_side.add_widget(name_food)
        right_side.add_widget(calories_of_food)
        right_side.add_widget(carbohydrate_of_food)
        right_side.add_widget(protein_of_food)
        right_side.add_widget(fat_of_food)
        right_side.add_widget(RICE)
        right_side.add_widget(TOTD)
        



        btn_side = BoxLayout(orientation = "horizontal",spacing = 10,size_hint = (1,.3))
        btn_side.add_widget(Button(text = "ADD FOOD",on_release = add_food,font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))
        
        btn_side.add_widget(Button(text = "MANAGE FOOD",on_release = themenu.to_AllFoodScreen,font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))
        btn_side.add_widget(Button(text = "DELETE ALL FOOD",on_release = self.deleteAllFood ,font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))



        input_layout.add_widget(left_side)
        input_layout.add_widget(right_side)
        screen = BoxLayout(orientation = "vertical", spacing = 15)
        screen.add_widget(Label(text = "ADD FOOD", color = (37/255, 64/255, 98/255, 1), font_size = 30, bold = True, size_hint = (1,.2)))
        screen.add_widget(input_layout)
        screen.add_widget(btn_side)
        screen.add_widget(Button(on_press = themenu.to_MainScreen,size_hint = (.8, .1),pos_hint = {'center_x':.5}, text = "Back",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= ''))
        self.add_widget(screen)
    def on_enter(self):
        self.load_size()
        self.main()

class AllFoodScreen(Screen):
   
    def main(self):
        f = open("Core\InOut\AllFood.txt","r")
        food = f.readlines()
        food = [s.replace("\n","") for s in food]
        mainWindow = GridLayout(cols = 1, spacing=30,size_hint_y=None)
        mainWindow.bind(minimum_height=mainWindow.setter('height'))
        def deleteFood(self):
            def delete(self):
                f = open("Core\InOut\deleteID.txt", "w")
                f.write(ID.text)
                f.close()
                noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Delete successful",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
                noti.open()
                os.chdir("Core")
                os.system("DeleteFood.exe")
                os.chdir("..")
                popUp.dismiss()
            btn = BoxLayout(orientation = "horizontal")
            btn.add_widget(Button(text = "Confirm", on_press = delete))
            btn.add_widget(Button(text = "Cancel", on_press = lambda *args: popUp.dismiss()))
            layout = BoxLayout(orientation = "vertical")
            layout.add_widget(Label(text = "Write an ID again to Confirm",color = (0,0,0,1)))
            ID = TextInput(multiline=False)
            layout.add_widget(ID)
            layout.add_widget(btn)
            popUp = Popup(content  = layout,
                    auto_dismiss = True,
                    size_hint = (.4 , .4),
                    pos_hint = {"center_x": .5, "center_y": .5},
                    background_color = (255,255,255,0.8),
                    title = "DID YOU WANT TO DELETE FOOD?",
                    title_color = (37/255, 64/255, 98/255, 1),
                    title_align = "center",
                    title_size = dp(20))
            popUp.open()
        x = 0
        for i in range(int(len(food)/10)):
            foodCard = BoxLayout(orientation = "horizontal", size_hint_y=None)
            icon = Image(source='meal-food-icon.png',size_hint = (0.25,None))
            foodCard.add_widget(icon)
            mainInformation = GridLayout(cols = 3)
            self.tod_string = ""
            if "1" in food[x+3]:
                self.have_rice = "Yes"
            else:
                self.have_rice = "No"
            if "1" in food[x+2]:
                self.tod_string = self.tod_string + "Morning, "
            if "2" in food[x+2]:
                self.tod_string = self.tod_string + "Noon, "
            if "3" in self.tod_string:
                self.tod_string = self.tod_string + "Afternoon"
                pass
            idLabel = Label(text = "ID: %s"%food[x],color = (0,0,0,1))
            nameLabel = Label(text = "Name: %s"%food[x+1],color = (0,0,0,1))
            TODLabel = Label(text = "Time Of Day: %s"%self.tod_string,color = (0,0,0,1))
            withRiceLabel = Label(text = "Rice: %s"%self.have_rice,color = (0,0,0,1))
            pickTimeLabel = Label(text = "Selected Time: %s"%food[x+4],color = (0,0,0,1))
            lastPickLabel = Label(text = "Last Selected: %s"%food[x+5],color = (0,0,0,1))
            caloriesLabel = Label(text = "Calories: %s"%food[x+6],color = (0,0,0,1))
            mainInformation.add_widget(idLabel)
            mainInformation.add_widget(nameLabel)
            mainInformation.add_widget(withRiceLabel)
            mainInformation.add_widget(Label())
            mainInformation.add_widget(TODLabel)
            mainInformation.add_widget(Label())
            mainInformation.add_widget(pickTimeLabel)
            mainInformation.add_widget(lastPickLabel)
            mainInformation.add_widget(caloriesLabel)
            foodCard.add_widget(mainInformation)
            btnDelete = Button(text = "Delete",font_size = dp(20),size_hint = (0.25,None),on_press = deleteFood)
            foodCard.add_widget(btnDelete)
            mainWindow.add_widget(foodCard)
            x+= 10
        scroll = ScrollView()
        scroll.add_widget(mainWindow)
        screen = BoxLayout(orientation = "vertical")
        popup = Popup(title = "MANAGE FOOD",title_align = "center",title_size = 40,title_color = (37/255, 64/255, 98/255, 1),size_hint=(1, 0.8),background_color = (255,255,255,1))
        popup.add_widget(scroll)
        screen.add_widget(popup)
        screen.add_widget(Button(on_press = themenu.to_FoodScreen ,size_hint = (.8, .05),pos_hint = {'center_x':.5}, text = "Back",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= ''))
        self.add_widget(screen)
        
    def resize_windows(self):
        Window.size = (size_screen_y,size_screen_x)
    def on_enter(self):
        self.resize_windows()
        self.main()
            
    

class MenuScreen(Screen):
    def re_run_core(self):
        os.chdir("Core")
        os.system("ActivateCore.exe")
        os.chdir("..")
        with open("Core\InOut\DailyFood.txt","r") as f:
            for i in range(7):
                B[i] = f.readline()
            for i in range(7):
                L[i] = f.readline()
            for i in range(7):
                D[i] = f.readline()
    
    def load_screen_size(self):
        Window.size = (size_screen_y,size_screen_x)

    def load_table(self):
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
        self.re_run_core()
        self.load_screen_size()
        self.load_table()




class AllFoodNutrientsScreen(Screen):
    def main(self):
        f = open("Core\InOut\AllFood.txt","r")
        food = f.readlines()
        food = [s.replace("\n","") for s in food]
        f.close()
        mainWindow = GridLayout(cols = 1, spacing=30,size_hint_y=None)
        mainWindow.bind(minimum_height=mainWindow.setter('height'))
        def deleteFood(self):
            def delete(self):
                f = open("Core\InOut\deleteID.txt", "w")
                f.write(ID.text)
                f.close()
                noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Delete successful",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
                noti.open()
                os.chdir("Core")
                os.system("DeleteFood.exe")
                os.chdir("..")
                popUp.dismiss()
            btn = BoxLayout(orientation = "horizontal")
            btn.add_widget(Button(text = "Confirm", on_press = delete))
            btn.add_widget(Button(text = "Cancel", on_press = lambda *args: popUp.dismiss()))
            layout = BoxLayout(orientation = "vertical")
            layout.add_widget(Label(text = "Write an ID again to Confirm",color = (0,0,0,1)))
            ID = TextInput(multiline=False)
            layout.add_widget(ID)
            layout.add_widget(btn)
            popUp = Popup(content  = layout,
                    auto_dismiss = True,
                    size_hint = (.4 , .4),
                    pos_hint = {"center_x": .5, "center_y": .5},
                    background_color = (255,255,255,0.8),
                    title = "DID YOU WANT TO DELETE FOOD?",
                    title_color = (37/255, 64/255, 98/255, 1),
                    title_align = "center",
                    title_size = dp(20))
            popUp.open()
        x = 0
        for i in range(int(len(food)/10)):
            foodCard = BoxLayout(orientation = "horizontal", size_hint_y=None)
            icon = Image(source='meal-food-icon.png',size_hint = (0.25,None))
            foodCard.add_widget(icon)
            mainInformation = GridLayout(cols = 3)
            self.tod_string = ""
            if "1" in food[x+3]:
                self.have_rice = "Yes"
            else:
                self.have_rice = "No"
            if "1" in food[x+2]:
                self.tod_string = self.tod_string + "Morning, "
            if "2" in food[x+2]:
                self.tod_string = self.tod_string + "Noon, "
            if "3" in self.tod_string:
                self.tod_string = self.tod_string + "Afternoon"
                pass
            idLabel = Label(text = "ID: %s"%food[x],color = (0,0,0,1))
            nameLabel = Label(text = "Name: %s"%food[x+1],color = (0,0,0,1))
            TODLabel = Label(text = "Time Of Day: %s"%self.tod_string,color = (0,0,0,1))
            withRiceLabel = Label(text = "Rice: %s"%self.have_rice,color = (0,0,0,1))
            pickTimeLabel = Label(text = "Selected Time: %s"%food[x+4],color = (0,0,0,1))
            lastPickLabel = Label(text = "Last Selected: %s"%food[x+5],color = (0,0,0,1))
            caloriesLabel = Label(text = "Calories: %s"%food[x+6],color = (0,0,0,1))
            carbLabel = Label(text = "Carbohydrate: %s"%food[x+7],color = (0,0,0,1))
            proteinLabel = Label(text = "Protein: %s"%food[x+8],color = (0,0,0,1))
            fatLabel = Label(text = "Fat: %s"%food[x+9],color = (0,0,0,1))
            mainInformation.add_widget(idLabel)
            mainInformation.add_widget(nameLabel)
            mainInformation.add_widget(withRiceLabel)
            mainInformation.add_widget(TODLabel)
            mainInformation.add_widget(caloriesLabel)
            mainInformation.add_widget(carbLabel)
            mainInformation.add_widget(proteinLabel)
            mainInformation.add_widget(fatLabel)
            foodCard.add_widget(mainInformation)
            btnDelete = Button(text = "Delete",font_size = dp(20),size_hint = (0.25,None),on_press = deleteFood)
            foodCard.add_widget(btnDelete)
            mainWindow.add_widget(foodCard)
            x+= 10
        scroll = ScrollView()
        scroll.add_widget(mainWindow)
        screen = BoxLayout(orientation = "vertical")
        popup = Popup(title = "MANAGE FOOD",title_align = "center",title_size = 40,title_color = (37/255, 64/255, 98/255, 1),size_hint=(1, 0.8),background_color = (255,255,255,1))
        popup.add_widget(scroll)
        screen.add_widget(popup)
        screen.add_widget(Button(on_press = themenu.to_FoodScreen ,size_hint = (.8, .05),pos_hint = {'center_x':.5}, text = "Back",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= ''))
        self.add_widget(screen)
        
    def resize_windows(self):
        Window.size = (size_screen_y,size_screen_x)
    def on_enter(self):
        self.resize_windows()
        self.main()
            




class NutrientsScreen(Screen):
    def load_screen_size(self):
        Window.size = (size_screen_x,size_screen_y)

    def main(self):

        with open("Core\InOut\TotalCalories.txt","r") as f:
            self.temp = f.readlines()
            self.temp = [x.replace("\n","") for x in self.temp]
            self.numberOfPeople = int(float(self.temp[0]))
            self.totalKcal = int(float(self.temp[1]))
        main_side = GridLayout(cols = 2)

        with open("Core\InOut\Properties.txt","r") as f:
            properties = f.readlines()
            properties = [s.replace("\n","") for s in properties]
            self.type = properties[0]
            self.diet = properties[1]
            self.diet = 1
            if(self.diet == 1):
                self.carbo = round(0.35 * self.totalKcal / 4)
                self.protein = round(0.43 * self.totalKcal / 4)
                self.fat = 0.22 * round(self.totalKcal / 9)
            if(self.diet == 2):
                self.carbo = round(0.25 * self.totalKcal / 4)
                self.protein = round(0.35 * self.totalKcal / 4)
                self.fat = round(0.4 * self.totalKcal / 9)
            if(self.diet == 3):
                self.carbo = round(0.7 * self.totalKcal / 4)
                self.protein = round(0.15 * self.totalKcal / 4)
                self.fat = round(0.15 * self.totalKcal / 9)


            main_side.add_widget(Label(text = "Number of family members",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
            main_side.add_widget(Label(text = "%s"%self.numberOfPeople,color = (0,0,0,1)))
            main_side.add_widget(Label(text = "Calories / day",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
            main_side.add_widget(Label(text = "%s"%self.totalKcal,color = (0,0,0,1)))
            main_side.add_widget(Label(text = "Carbohydrate / day",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
            main_side.add_widget(Label(text = "%s"%self.carbo,color = (0,0,0,1)))
            main_side.add_widget(Label(text = "Protein / day",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
            main_side.add_widget(Label(text = "%s"%self.protein,color = (0,0,0,1)))
            main_side.add_widget(Label(text = "Fat / day",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
            main_side.add_widget(Label(text = "%s"%self.fat,color = (0,0,0,1)))
            main_side.add_widget(Label(text = "Current Diet",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
            main_side.add_widget(Label(text = "%s"%self.diet,color = (0,0,0,1)))
            main_side.add_widget(Label(text = "Current type of menu",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
            main_side.add_widget(Label(text = "%s"%self.type,color = (0,0,0,1)))

        

        def HelpType(event):
            layout = BoxLayout(orientation = "vertical")
            l1 = Label(color = (0,0,0,1) ,text = "Works well in single-user menu")
            l1.bind(size = lambda s,w: s.setter('text_size')(s,w))
            layout.add_widget(l1)
            l2 = Label(color = (0,0,0,1) ,text = "If making a menu for family, choose normal")
            l2.bind(size=lambda s,w : s.setter('text_size')(s,w))
            layout.add_widget(l2)
            helpPopUp = Popup(title = "HELP",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = layout, auto_dismiss = True, size_hint = (0.4,0.2))
            helpPopUp.open()
        def takeType(value):
            with open("Core\InOut\Properties.txt","r") as f:
                properties = f.rlines()
                properties = [s.replace("\n","") for s in properties]
                self.type = properties[0]
                self.diet = properties[1]
            if value == "Gain Weight" :
                self.type = 1
            elif value == "Loss Weight" :
                self.type = 2
            elif value == "Normal" :
                self.type = 3
            with open("Core\InOut\Properties.txt","w") as f:
                f.write(str(self.type))
                f.write("\n")
                f.write(str(self.diet))
            noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Change successful",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
            noti.open()

        
        typeMenu = DropDown()
        #gain weight/loss weight/normal
        Gw = Button(text = "Gain Weight",background_normal = "", background_color = (132/255,166/255,207/255,1),size_hint_y = None, height = 35, on_release = lambda type: takeType(value = type.text))
        Gw.bind(on_release = lambda Gw: typeMenu.select(Gw.text))
        Lw = Button(text = "Loss Weight",background_normal = "", background_color = (132/255,166/255,207/255,1),size_hint_y = None, height = 35, on_release = lambda type: takeType(value = type.text))
        Lw.bind(on_release = lambda Lw: typeMenu.select(Lw.text))
        Nw = Button(text = "Normal",background_normal = "", background_color = (132/255,166/255,207/255,1),size_hint_y = None, height = 35, on_release = lambda type: takeType(value = type.text))
        Nw.bind(on_release = lambda Nw: typeMenu.select(Nw.text))
        Help = Button(text = "Help",background_normal = "", background_color = (132/255,166/255,207/255,1),size_hint_y = None, height = 35, on_release = lambda type: HelpType(event=open))
        typeMenu.add_widget(Gw)
        typeMenu.add_widget(Nw)
        typeMenu.add_widget(Lw)
        typeMenu.add_widget(Help)
        btnType = Button(text = "Choose Type",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= '')
        btnType.bind(on_release = typeMenu.open)
        typeMenu.bind(on_select = lambda instance, x: setattr(btnType, "text", x))



        def HelpDiet(event):
            layout = BoxLayout(orientation = "vertical")
            l1 = Label(color = (0,0,0,1) ,text = "Works well in single-user menu")
            l1.bind(size = lambda s,w: s.setter('text_size')(s,w))
            layout.add_widget(l1)
            l2 = Label(color = (0,0,0,1) ,text = "If making a menu for family, choose normal")
            l2.bind(size=lambda s,w : s.setter('text_size')(s,w))
            layout.add_widget(l2)
            helpPopUp = Popup(title = "HELP",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = layout, auto_dismiss = True, size_hint = (0.4,0.2))
            helpPopUp.open()
        def takeDiet(value):
            with open("Core\InOut\Properties.txt","r") as f:
                properties = f.readlines()
                properties = [s.replace("\n","") for s in properties]
                for x in properties:
                    self.type = properties[0]
                    global diet 
                    self.diet = properties[1]
            if value == "Rich Protein" :
                self.diet = 1
            elif value == "Rich Fat" :
                self.diet = 2
            elif value == "Rich Carb" :
                self.diet = 3
            with open("Core\InOut\Properties.txt","w") as f:
                f.write(str(self.type))
                f.write("\n")
                f.write(str(self.diet))
            noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Change successful",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
            noti.open()
        dietMenu = DropDown()
        #gain weight/loss weight/normal
        Rp = Button(text = "Rich Protein",background_normal = "", background_color = (132/255,166/255,207/255,1),size_hint_y = None, height = 35, on_release = lambda diet: takeDiet(value = diet.text))
        Rp.bind(on_release = lambda Rp: dietMenu.select(Rp.text))
        Rf = Button(text = "Rich Fat",background_normal = "", background_color = (132/255,166/255,207/255,1),size_hint_y = None, height = 35, on_release = lambda diet: takeDiet(value = diet.text))
        Rf.bind(on_release = lambda RfLc: dietMenu.select(Rf.text))
        Rc = Button(text = "Normal",background_normal = "", background_color = (132/255,166/255,207/255,1),size_hint_y = None, height = 35, on_release = lambda diet: takeDiet(value = diet.text))
        Rc.bind(on_release = lambda Rc: dietMenu.select(Rc.text))
        Help = Button(text = "Help",background_normal = "", background_color = (132/255,166/255,207/255,1),size_hint_y = None, height = 35, on_release = lambda diet: HelpDiet(event=open))
        dietMenu.add_widget(Rp)
        dietMenu.add_widget(Rf)
        dietMenu.add_widget(Rc)
        dietMenu.add_widget(Help)
        btnDiet = Button(text = "Choose Diet",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= '')
        btnDiet.bind(on_release = dietMenu.open)
        dietMenu.bind(on_select = lambda instance, x: setattr(btnDiet, "text", x))




        







        func_side = BoxLayout(orientation = "horizontal", size_hint = (1,.3), spacing = 5)
        func_side.add_widget(Button(text = "All Food",on_release = themenu.to_nutrientsAllfood,font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= ''))
        func_side.add_widget(btnType)
        func_side.add_widget(btnDiet)



        screen = BoxLayout(orientation = "vertical", spacing = 15)
        screen.add_widget(Label(text = "ADD MEMBER", color = (37/255, 64/255, 98/255, 1), font_size = 30, bold = True, size_hint = (1,.2)))
        screen.add_widget(main_side)
        screen.add_widget(func_side)
        screen.add_widget(Button(on_release = themenu.to_MainScreen,size_hint = (.8, .1),pos_hint = {'center_x':.5}, text = "Back",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= ''))

        self.add_widget(screen)
        return screen

    def on_enter(self):
        self.load_screen_size()
        self.main()


class MainScreen(Screen):
    def load_size(self):
        Window.size = (size_screen_x,size_screen_y)
    def on_enter(self):
        self.load_size()
    def developing(self):
        noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Developing",color = (0,0,0,1.00),), auto_dismiss = True, size_hint = (0.5,0.2))
        noti.open()
        pass
    def picknow_button_on(self):
        self.ids.image_picknow.source = "Core/image/UI/ChooseIcon/PickNowChoose.png"
    def picknow_button_release(self):
        self.ids.image_picknow.source = "Core/image/UI/ButtonOfUI/ButtonPickNow.png"
        self.developing()
    def nutrients_button_on(self):
        self.ids.image_nutrients.source = "Core/image/UI/ChooseIcon/NutriChoose.png"
    def nutrients_button_release(self):
        self.ids.image_nutrients.source = "Core/image/UI/ButtonOfUI/ButtonNutrients.png"
        themenu.sm.current = "nutrients"
    def addfood_button_on(self):
        self.ids.image_addfood.source = "Core/image/UI/ChooseIcon/AddFoodchoose.png"
    def addfood_button_release(self):
        self.ids.image_addfood.source = "Core/image/UI/ButtonOfUI/ButtonAddFood.png"
        themenu.sm.current = 'food'
    def addfamily_button_on(self):
        self.ids.image_addfamily.source = "Core/image/UI/ChooseIcon/AddFamilychoose.png"
    def addfamily_button_release(self):
        self.ids.image_addfamily.source = "Core/image/UI/ButtonOfUI/ButtonAddFamily.png"
        themenu.sm.current = "user"
    def menu_button_on(self):
        self.ids.image_menu.source = "Core/image/UI/ChooseIcon/Menuchoose.png"
    def menu_button_release(self):
        self.ids.image_menu.source = "Core/image/UI/ButtonOfUI/ButtonMenu.png"
        themenu.sm.current = 'menu'
    def order_button_on(self):
        self.ids.image_order.source = "Core/image/UI/ChooseIcon/OrderChoose.png"
    def order_button_release(self):
        self.ids.image_order.source = "Core/image/UI/ButtonOfUI/ButtonOrder.png"
        self.developing()


class MyApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.main_screen = MainScreen(name = "main")
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(UserScreen(name = "user"))
        self.sm.add_widget(FoodScreen(name = "food"))
        self.sm.add_widget(MenuScreen(name = "menu"))
        self.sm.add_widget(AllFoodScreen(name = "allfood"))
        self.sm.add_widget(NutrientsScreen(name = "nutrients"))
        self.sm.add_widget(AllFoodNutrientsScreen(name = "nutrientsAllfood"))
        return self.sm
    def to_MainScreen(self,b):
        themenu.sm.current = "main"
    def to_FoodScreen(a,b):
        themenu.sm.current = "food"
    def to_AllFoodScreen(a,b):
        themenu.sm.current = "allfood"
    def to_Nutrient(a,b):
        themenu.sm.current = "nutrients"
    def to_nutrientsAllfood(a,b):
        themenu.sm.current = "nutrientsAllfood"




if "_name_" == "_name_":
    themenu = MyApp()
    themenu.run() 