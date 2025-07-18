from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
import random
Window.clearcolor = (1,1,1,1)


class diceroller(App):
    def build(self):
        self.boxlayout = BoxLayout(orientation = "vertical",  spacing = 20 , padding = 50)
        self.diceshow = Label(text = "Roll the dice to see what you get" ,color = (0,0,0,1) , font_size = "24sp" , markup =True)
        self.label = Label(text = "Dice Roller" , bold= True , color=(0,0,0,1) , font_size = "32sp")

        self.image = Image(source=r"C:\Users\Ali hassan\Desktop\Dice roller\assets\1.png" ,size_hint = (None , None) , size = (250, 250), allow_stretch = True , pos_hint = {"center_x" : 0.5} )

        self.button = Button(text = "Roll Dice" , on_press =  self.buttonpressed)




        self.boxlayout.add_widget(self.label)
        self.boxlayout.add_widget(self.diceshow)
        self.boxlayout.add_widget(self.image)
        self.boxlayout.add_widget(self.button)



        return self.boxlayout


    def buttonpressed(self , instance):
        random_num = random.randint(1,6)
        newnum = str(random_num)

        self.diceshow.text = f"You rolled [b]{newnum}[/b]"

        
        self.image.source =  fr"C:/Users/Ali hassan/Desktop/Dice roller/assets/{random_num}.png"   

if __name__ == "__main__":
    diceroller().run()

