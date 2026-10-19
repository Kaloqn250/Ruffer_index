from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):
        layout = FloatLayout()

        btn1 = Button(
            text = 'Button 1',
            # size_hint = (None, None),
            #             #x   y
            # height = 500,
            # width = 1300,

            size_hint = (0.3, 0.3),
            # size_hint_y = 0.3


            pos_hint = {
                # 'x': 0,   #left
                # 'y': 0    #bottom
                'center_x': 0.35, 
                'center_y': 0.65

                # 'top': 1,
                # 'right': 1
            }
        )

        btn2 = Button(
            text= 'Button 2',
            size_hint = (0.3, 0.3),
            pos_hint = {
                'center_x': 0.65,
                'center_y': 0.35
            }
        )

        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout


app = MyApp()
app.run()