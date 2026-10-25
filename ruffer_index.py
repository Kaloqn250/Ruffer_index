from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

results = {}
result_text = 'this is the result text'
class FirstScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.screen_layout = FloatLayout()
        self.add_widget(self.screen_layout)
       
        text_label = Label(
            text = 'This allows us to \n' \
            'carry out an initial diagnostics of your health \n' \
            'using a Ruffier test.',

            pos_hint = {
                'center_x': 0.5,
                'center_y': 0.7
            }
        )

        self.screen_layout.add_widget(text_label)

        self.name_label = Label(
            text = 'Enter your name:',
            pos_hint={
                'center_x': 0.25,
                'center_y': 0.35
            }
        )

        self.age_label = Label(
            text = 'Enter your age:',
            pos_hint={
                'center_x': 0.25,
                'center_y': 0.25
            }   
        )

        self.screen_layout.add_widget(self.name_label)
        self.screen_layout.add_widget(self.age_label)

        self.name_input = TextInput(
            size_hint = (0.3, 0.05),
            pos_hint = {
                'center_x': 0.6,
                'center_y': 0.35
            }
        )
        self.age_input = TextInput(
            size_hint = (0.3, 0.05),
            pos_hint = {
                'center_x': 0.6,
                'center_y': 0.25
            }
        )

        self.screen_layout.add_widget(self.name_input)
        self.screen_layout.add_widget(self.age_input)

        btn = Button(
            text = 'Continue',
            size_hint = (0.3, 0.15),
            pos_hint = {
                'center_x': 0.5,
                'center_y': 0.1
            }
        )

        btn.on_press = self.save_and_continue

        self.screen_layout.add_widget(btn)

      


    def save_and_continue(self, ):
        results['name'] = self.name_input.text
        results['age'] = self.age_input.text
        self.manager.current = 'second'



       


class SecondScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = FloatLayout()

        text1 = Label(
            text= 'Mesure your pulse for 15 seconds \n' \
            'Write the result in the box bellow.' ,
            pos_hint = {
                'center_x': 0.5,
                'center_y': 0.5
            }
        )

        text2 = Label(
            text = 'Enter the result: ',
            pos_hint = {
                'center_x': 0.3,
                'center_y': 0.3
            }

        )

        self.pulse_input = TextInput(
            size_hint = (0.3, 0.05),
            pos_hint = {
                'center_x': 0.6,
                'center_y': 0.3
                        }
        )

        btn = Button(
                    text = 'Continue',
                    size_hint = (0.3, 0.15),
                    pos_hint = {
                        'center_x': 0.5,
                        'center_y': 0.1
                    }
                )

        btn.on_press = self.save_and_continue

        layout.add_widget(text1)
        layout.add_widget(text2)
        layout.add_widget(self.pulse_input)
        layout.add_widget(btn)

        self.add_widget(layout)

    def save_and_continue(self):
        results['first_measure'] = self.pulse_input.text
        self.manager.current = 'third'



class ThirdScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = FloatLayout()

        label = Label(text='Do 30 squats in 45 seconds')
        btn = Button(
            text = 'Continue',
            size_hint = (0.3, 0.15),
            pos_hint = {
                'center_x': 0.5,
                'center_y': 0.1
            }
        )

        btn.on_press = self.btn_continue

        layout.add_widget(label)
        layout.add_widget(btn)


        self.add_widget(layout)

    def btn_continue(self):
        self.manager.current = 'fourth'



class FourthScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = FloatLayout()

        text = Label(
            text= 'Measure your pulse twice in the next minute \n' \
            'during the firsdt 15 seconds, and in the last 15 seconds \n' \
            'Write the results bellow'
        )

        result_1 = Label(
            text='First result: ',
            pos_hint={
                'center_x': 0.25,
                'center_y': 0.35
                        }
        )
        result_2 = Label(
            text='Second result: ',
            pos_hint={
                'center_x': 0.25,
                'center_y': 0.25
                        }
        )

        self.res_1_input = TextInput(
            size_hint = (0.3, 0.05),
            pos_hint = {
                'center_x': 0.6,
                'center_y': 0.35
            }
        )
        self.res_2_input = TextInput(
            size_hint = (0.3, 0.05),
            pos_hint = {
            'center_x': 0.6,
            'center_y': 0.25
            }
        )

        btn = Button(
            text = 'Continue',
            size_hint = (0.3, 0.15),
            pos_hint = {
                'center_x': 0.5,
                'center_y': 0.1
                }
            )

        btn.on_press = self.save_and_continue

        layout.add_widget(text)
        layout.add_widget(result_1)
        layout.add_widget(result_2)
        layout.add_widget(self.res_1_input)
        layout.add_widget(self.res_2_input)
        layout.add_widget(btn)


        self.add_widget(layout)

    def save_and_continue(self):
        results['second_measure'] = self.res_1_input.text
        results['third_measure'] = self.res_2_input.text

        print(results.items())


        self.manager.current = 'fifth'



class FifthScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = FloatLayout()

        self.result_label= Label(text='')

        layout.add_widget(self.result_label)

        self.add_widget(layout)

    def on_pre_enter(self, *args):
        self.show_results()

    def show_results(self):
        p1 = int(results['first_measure'])
        p2 = int(results['second_measure'])
        p3 = int(results['third_measure'])
        index = (4 * (p1 + p2 + p3) - 200) / 10

        text = ''
        if index <= 3:
            text = 'Perfect condition'

        elif index <= 6:
            text = 'Good condition'

        elif index <= 9:
            text = 'Not the best you can have'

        elif index <= 14:
            text = 'Not very good condition'

        else:
            text = 'Go to see a doctor'


        self.result_label.text = f'\n\
            Name: {results.get('name')}\n\
            Age: {results["age"]}\n\
            Result from the test: {text}'


        # btn = Button(
        #     text='start',
        #     size_hint = (1, 0.2)
        #              )
        # btn.on_press = 


    # def


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