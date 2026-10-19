from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

results = {}

class FirstScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = FloatLayout()
        self.add_widget(layout)

        text_label = Label(
            text = 'This allows us to \n' \
            'carry out an initial diagnostics of your health \n' \
            'using a Ruffier test.',

            pos_hint = {
                'center_x': 0.5,
                'center_y': 0.7
            }
        )

        layout.add_widget(text_label)

        name_label = Label(
            text = 'Enter your name:',
            pos_hint={
                'center_x': 0.25,
                'center_y': 0.35
            }
        )

        age_label = Label(
            text = 'Enter your age:',
            pos_hint={
                'center_x': 0.25,
                'center_y': 0.25
            }   
        )

        layout.add_widget(name_label)
        layout.add_widget(age_label)

        name_input = TextInput(
            size_hint = (0.3, 0.05),
            pos_hint = {
                'center_x': 0.6,
                'center_y': 0.35
            }
        )
        age_input = TextInput(
            size_hint = (0.3, 0.05),
            pos_hint = {
                'center_x': 0.6,
                'center_y': 0.25
            }
        )

        layout.add_widget(name_input)
        layout.add_widget(age_input)

        btn = Button(
            text = 'Continue',
            size_hint = (0.3, 0.15),
            pos_hint = {
                'center_x': 0.5,
                'center_y': 0.1
            }
        )

        btn.on_press = self.save_and_continue

        layout.add_widget(btn)

      


    def save_and_continue(self, ):
        results['name'] = self.name_input.text
        results['age'] = self.age_input.text
        self.manager.current = 'second'

        print(results.items())


       


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class FourthScreen(Screen):
    pass


class FifthScreen(Screen):
    pass

class RufferIndex(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        sm.add_widget(FifthScreen(name='fifth'))

        return sm


app = RufferIndex()
app.run()