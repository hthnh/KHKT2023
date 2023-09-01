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

from kivy.uix.image import Image

from kivy.uix.scrollview import ScrollView

from kivy.uix.popup import Popup

from kivy.uix.gridlayout import GridLayout

from kivy.metrics import dp

from datetime import date
today = date.today()

import time

from kivy.core.window import Window

import os
path_to = os.getcwd()
os.chdir(path_to)
os.chdir("Core\InOut")
if os.path.getsize("TotalCalories.txt") != 0 :
    os.chdir("..")
    os.system("ActivateCore.exe")
else:
    os.chdir("..")

os.chdir("..")
 

import pyuac
if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()


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
        sm.add_widget(AllFoodScreen(name = "allfood"))
        return sm

class UserScreen(Screen):
    def load_size(self):
        Window.size = (600,901)
    def back_screen(a, b):
        sm.current ='main'
    
    def main(self):
        input_layout = BoxLayout(orientation = 'horizontal')
        left_side = BoxLayout(orientation = "vertical",spacing = 20)
        right_side = BoxLayout(orientation = "vertical", spacing = 20)
        
        left_side.add_widget(Label(text = "GENDER INENTIFY",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "AGE",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "WEIGHT",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "HEIGHT",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "CURRENT STATUS",font_size = 23,bold = True, color =(0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "TYPE OF MENU",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))



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
            helpPopUp = Popup(title = "Help",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = layout, auto_dismiss = True, size_hint = (0.675,0.5))
            helpPopUp.open()
        
        Style = DropDown()

        one = Button(text = "office work",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        one.bind(on_release = lambda one: Style.select(one.text))
        Style.add_widget(one)

        two = Button(text = "outdoor work",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        two.bind(on_release = lambda two: Style.select(two.text))
        Style.add_widget(two)

        three = Button(text = "exercise sometimes",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        three.bind(on_release = lambda three: Style.select(three.text))
        Style.add_widget(three)
        
        four = Button(text = "always exercise",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        four.bind(on_release = lambda four: Style.select(four.text))
        Style.add_widget(four)

        five = Button(text = "athlete",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: takeStyle(value=style.text))
        five.bind(on_release = lambda five: Style.select(five.text))
        Style.add_widget(five)

        helpStyle = Button(text = "Help",background_normal = "", background_color = (132/255,166/255,207/255,1), size_hint_y = None, height = 35, on_release= lambda style: HelpStyle(event = open))
        Style.add_widget(helpStyle)

        btnStyle = Button(text = "Choice your life style",background_normal = "", background_color = (132/255,166/255,207/255,1))
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
            helpPopUp = Popup(title = "HELP",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = layout, auto_dismiss = True, size_hint = (0.4,0.2))
            helpPopUp.open()

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

        btnType = Button(text = "Choice type of menu",background_normal = "", background_color = (132/255,166/255,207/255,1))
        btnType.bind(on_release = typeMenu.open)
        typeMenu.bind(on_select = lambda instance, x: setattr(btnType, "text", x))


        def check_add_user(self):
            if sex == 1 or sex == 0 :
                if not "age" in age.text :
                    if not "kg" in weight.text :
                        if not "cm" in height.text :
                            if style == 1 or style == 2 or style == 3 or style == 4 or style == 5 :
                                if type == 1 or type == 2 or type == 3 :
                                    AddUser()
                                else :
                                    noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Missing Type",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
                                    noti.open()
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
        right_side.add_widget(btnType)


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
        screen.add_widget(Button(on_press = self.back_screen,size_hint = (.8, .1),pos_hint = {'center_x':.5}, text = "Back",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= ''))

        self.add_widget(screen)
        return screen
    def on_enter(self):
        self.load_size()
        self.main()


class FoodScreen(Screen):
    def load_size(self):
        Window.size = (600,901)
    def back_screen(a, b):
        sm.current ='main'

    def main(self):
        input_layout = BoxLayout(orientation = 'horizontal')
        left_side = BoxLayout(orientation = "vertical",spacing = 20)
        right_side = BoxLayout(orientation = "vertical", spacing = 20)

        left_side.add_widget(Label(text = "NAME FOOD",font_size = 23,bold = True, color = (0, 0, 0, 1), font_family = 'Core/image/UI/Text/Noto_Serif'))
        left_side.add_widget(Label(text = "CALORIES",font_size = 23,bold = True, color = (0, 0, 0, 1),font_family = 'Core/image/UI/Text/Noto_Serif'))
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
           
            noti = Popup(title = "NOTIFICATION",title_color = (37/255, 64/255, 98/255, 1),background_color = (255,255,255,1),title_align = "center",content = Label(text = "Add successful",color = (0,0,0,1)), auto_dismiss = True, size_hint = (0.4,0.15))
            noti.open()



        

        global name_food
        name_food = TextInput(text = "name",multiline = False,background_normal = "", background_color = (132/255,166/255,207/255,0.8))
        global calories_of_food
        calories_of_food = TextInput(text = "calories",multiline = False,background_normal = "", background_color = (132/255,166/255,207/255,0.8))


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
        right_side.add_widget(RICE)
        right_side.add_widget(TOTD)
        



        btn_side = BoxLayout(orientation = "horizontal",spacing = 10,size_hint = (1,.3))
        btn_side.add_widget(Button(text = "ADD FOOD",on_release = add_food,font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))
        def open_screen_allfood(b):
            sm.current = 'allfood'
        btn_side.add_widget(Button(text = "MANAGE FOOD",on_release = open_screen_allfood,font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))
        btn_side.add_widget(Button(text = "DELETE ALL FOOD",font_size = 15,background_normal = "", background_color = (37/255, 64/255, 98/255, 1)))



        input_layout.add_widget(left_side)
        input_layout.add_widget(right_side)
        screen = BoxLayout(orientation = "vertical", spacing = 15)
        screen.add_widget(Label(text = "ADD FOOD", color = (37/255, 64/255, 98/255, 1), font_size = 30, bold = True, size_hint = (1,.2)))
        screen.add_widget(input_layout)
        screen.add_widget(btn_side)
        screen.add_widget(Button(on_press = self.back_screen,size_hint = (.8, .1),pos_hint = {'center_x':.5}, text = "Back",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= ''))
        self.add_widget(screen)
        return screen
    def on_enter(self):
        self.load_size()
        self.main()

class AllFoodScreen(Screen):
    def back_screen(a, b):
        sm.current ='main'
    def main(self):
        f = open("Core\InOut\AllFood.txt","r")
        food = f.readlines()
        food = [s.replace("\n","") for s in food]
        mainWindow = GridLayout(cols = 1, spacing=10,size_hint_y=None)
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
                Allfood.dismiss()
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
        for i in range(int(len(food)/7)):
            foodCard = BoxLayout(orientation = "horizontal", size_hint_y=None)
            icon = Image(source='meal-food-icon.png',size_hint = (0.25,None))
            foodCard.add_widget(icon)
            mainInformation = GridLayout(cols = 3)
            idLabel = Label(text = "ID: %s"%food[x],color = (0,0,0,1))
            nameLabel = Label(text = "Name: %s"%food[x+1],color = (0,0,0,1))
            TODLabel = Label(text = "Time Of Day: %s"%food[x+2],color = (0,0,0,1))
            withRiceLabel = Label(text = "Rice: %s"%food[x+3],color = (0,0,0,1))
            pickTimeLabel = Label(text = "Selected Time: %s"%food[x+4],color = (0,0,0,1))
            lastPickLabel = Label(text = "Last Selected: %s"%food[x+5],color = (0,0,0,1))
            caloriesLabel = Label(text = "Calories: %s"%food[x+6],color = (0,0,0,1))
            mainInformation.add_widget(idLabel)
            mainInformation.add_widget(nameLabel)
            mainInformation.add_widget(TODLabel)
            mainInformation.add_widget(withRiceLabel)
            mainInformation.add_widget(pickTimeLabel)
            mainInformation.add_widget(lastPickLabel)
            mainInformation.add_widget(caloriesLabel)
            foodCard.add_widget(mainInformation)
            btnDelete = Button(text = "Delete",font_size = dp(20),size_hint = (0.25,None),on_press = deleteFood)
            foodCard.add_widget(btnDelete)
            mainWindow.add_widget(foodCard)
            x+= 7
        scroll = ScrollView(size_hint=(1, 0.8))
        scroll.add_widget(mainWindow)
        screen = BoxLayout(orientation = "vertical")
        screen.add_widget(scroll)
        screen.add_widget(Button(on_press = self.back_screen,size_hint = (.8, .1),pos_hint = {'center_x':.5}, text = "Back",font_size = 30, background_color = (37/255, 64/255, 98/255, 1), background_normal= ''))
        self.add_widget(screen)
        
    def resize_windows(self):
        Window.size = (901,600)
    def on_enter(self):
        self.resize_windows()
        self.main()
            
    
class MainScreen(Screen):
    def load_size(self):
        Window.size = (600,901)
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
        self.developing()
    def addfood_button_on(self):
        self.ids.image_addfood.source = "Core/image/UI/ChooseIcon/AddFoodchoose.png"
    def addfood_button_release(self):
        self.ids.image_addfood.source = "Core/image/UI/ButtonOfUI/ButtonAddFood.png"
        sm.current = 'food'
    def addfamily_button_on(self):
        self.ids.image_addfamily.source = "Core/image/UI/ChooseIcon/AddFamilychoose.png"
    def addfamily_button_release(self):
        self.ids.image_addfamily.source = "Core/image/UI/ButtonOfUI/ButtonAddFamily.png"
        sm.current = "user"
    def menu_button_on(self):
        self.ids.image_menu.source = "Core/image/UI/ChooseIcon/Menuchoose.png"
    def menu_button_release(self):
        self.ids.image_menu.source = "Core/image/UI/ButtonOfUI/ButtonMenu.png"
        sm.current = 'menu'
    def order_button_on(self):
        self.ids.image_order.source = "Core/image/UI/ChooseIcon/OrderChoose.png"
    def order_button_release(self):
        self.ids.image_order.source = "Core/image/UI/ButtonOfUI/ButtonOrder.png"
        self.developing()
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