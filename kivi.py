from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout  
from kivy.uix.switch import Switch
from kivy.uix.filechooser import FileChooser
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner 
import random  

class MyApp(App):
    def build(self):
        button = Button(text = "U nigar")
        self.label = Label(text = 'Milfa')
        switch = Switch()
        popup = Popup()
        spinner = Spinner()
        filechooser = FileChooser()
        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(button)
        layout.add_widget(self.label)
        layout.add_widget(switch)
        layout.add_widget(spinner)
        layout.add_widget(filechooser)
        
        button.bind(on_press = self.click_button)
        return layout
    
    

    def click_button(self, instance):
        a = ''
        for i in range(8):
            a += str(random.randint(0,10))
        self.label.text = a

    

if __name__ == '__main__':
    MyApp().run()