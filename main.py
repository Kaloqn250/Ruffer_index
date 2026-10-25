from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager


class ScrButton(Button):
    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen #FirstScreen
        self.direction = direction #right
        self.goal = goal #main

    def on_press(self):
        self.screen.manager.transition.direction = self.direction 
        self.screen.manager.current = self.goal

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_box = BoxLayout()
        label = Label(text='Main Screen')
        main_box.add_widget(label)

        secondary_box = BoxLayout(orientation='vertical')

        btn1 = ScrButton(screen=self, direction='left', goal='first', text='Go to First Screen')
        btn2 = ScrButton(screen=self, direction='right', goal='second', text='Go to Second Screen')
        btn3 = ScrButton(screen=self, direction='up', goal='third', text='Go to Third Screen')
        btn4 = ScrButton(screen=self, direction='down', goal='fourth', text='Go to Fourth Screen')

        secondary_box.add_widget(btn1)
        secondary_box.add_widget(btn2)
        secondary_box.add_widget(btn3)
        secondary_box.add_widget(btn4)

        main_box.add_widget(secondary_box)
        self.add_widget(main_box)


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout()

        label = Label(text='First Screen')
        btn = ScrButton(screen=self, direction='right', goal='main', text='Go Back to Main Screen')
        box.add_widget(btn)
        box.add_widget(label)

        self.add_widget(box)
        
        


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout()

        label = Label(text='Second Screen')
        btn = ScrButton(screen=self, direction='left', goal='main', text='Go Back to Main Screen')
        box.add_widget(label)
        box.add_widget(btn)

        self.add_widget(box)


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation='vertical')

        label = Label(text='Third Screen')
        btn = ScrButton(screen=self, direction='down', goal='main', text='Go Back to Main Screen')
        box.add_widget(btn)
        box.add_widget(label)

        self.add_widget(box)


class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation='vertical')

        label = Label(text='Fourth Screen')
        btn = ScrButton(screen=self, direction='up', goal='main', text='Go Back to Main Screen')
        box.add_widget(label)
        box.add_widget(btn)

        self.add_widget(box)




class Instagram(App):
    def build(self):
       sm = ScreenManager()
       sm.add_widget(MainScreen(name='main'))
       sm.add_widget(FirstScreen(name='first'))
       sm.add_widget(SecondScreen(name='second'))
       sm.add_widget(ThirdScreen(name='third'))
       sm.add_widget(FourthScreen(name='fourth'))
       return sm
    
    
app = Instagram()
app.run()