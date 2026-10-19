# Импортираме класа App, който използваме за създаване и стартиране на приложението.
from kivy.app import App

# Импортираме Screen за създаване на екрани и ScreenManager за управлението им.
from kivy.uix.screenmanager import Screen, ScreenManager

# Импортираме FloatLayout, който позволява да позиционираме елементите чрез координати и пропорции.
from kivy.uix.floatlayout import FloatLayout

# Импортираме Button за създаване на бутони.
from kivy.uix.button import Button

# Импортираме Label за показване на текст.
from kivy.uix.label import Label

# Импортираме TextInput за въвеждане на текст от потребителя.
from kivy.uix.textinput import TextInput

# Създаваме празен речник, в който ще съхраняваме въведените данни.
# Той е извън класовете, затова може да бъде използван от различни екрани.
results = {}

# Създаваме клас за първия екран.
# Той наследява Screen, защото представлява отделен екран в приложението.
class FirstScreen(Screen):

    # Методът __init__ се изпълнява при създаването на обект от класа.
    # **kw позволява да приемаме допълнителни именувани аргументи,
    # например name='first'.
    def __init__(self, **kw):

        # Извикваме конструктора на родителския клас Screen.
        # Така се изпълнява необходимата начална настройка на екрана.
        super().__init__(**kw)

        # Създаваме FloatLayout, в който ще разположим елементите.
        self.screen_layout = FloatLayout()

        # Добавяме оформлението към текущия екран.
        self.add_widget(self.screen_layout)

                # Създаваме Label, който ще показва описание на теста.
        text_label = Label(

            # text задава съдържанието на текста.
            # Символът \n преминава на нов ред.
            text = 'This allows us to \n' \
            'carry out an initial diagnostics of your health \n' \
            'using a Ruffier test.',

            # pos_hint определя позицията на елемента
            # чрез пропорции спрямо размера на родителското оформление.
            pos_hint = {
                'center_x': 0.5,  # Центърът по хоризонтала е на 50%.
                'center_y': 0.7   # Центърът по вертикала е на 70%.
            }
        )

        # Добавяме Label към FloatLayout, за да се покаже на екрана.
        self.screen_layout.add_widget(text_label)

                # Създаваме етикет, който подканва потребителя да въведе името си.
        self.name_label = Label(
            text = 'Enter your name:',

            # Позиционираме етикета чрез центъра му.
            pos_hint = {
                'center_x': 0.25,
                'center_y': 0.35
            }
        )

        # Създаваме етикет, който подканва потребителя да въведе възрастта си.
        self.age_label = Label(
            text = 'Enter your age:',
            pos_hint = {
                'center_x': 0.25,
                'center_y': 0.25
            }
        )

        # Добавяме двата етикета към оформлението.
        self.screen_layout.add_widget(self.name_label)
        self.screen_layout.add_widget(self.age_label)

                # Създаваме поле, в което потребителят ще въведе името си.
        self.name_input = TextInput(

            # size_hint определя относителните ширина и височина.
            # 0.3 означава 30% от ширината, а 0.05 – 5% от височината
            # на родителското оформление.
            size_hint = (0.3, 0.05),

            # Определяме позицията на полето.
            pos_hint = {
                'center_x': 0.6,
                'center_y': 0.35
            }
        )

        # Създаваме поле за въвеждане на възрастта.
        self.age_input = TextInput(
            size_hint = (0.3, 0.05),
            pos_hint = {
                'center_x': 0.6,
                'center_y': 0.25
            }
        )

        # Добавяме двете полета към оформлението.
        self.screen_layout.add_widget(self.name_input)
        self.screen_layout.add_widget(self.age_input)

                # Създаваме бутон, чрез който потребителят ще продължи към следващия екран.
        btn = Button(
            text = 'Continue',

            # Задаваме относителния размер на бутона.
            size_hint = (0.3, 0.15),

            # Поставяме бутона в долната част на екрана.
            pos_hint = {
                'center_x': 0.5,
                'center_y': 0.1
            }
        )

        # Свързваме събитието on_press с метода save_and_continue.
        # При натискане на бутона този метод ще бъде изпълнен.
        btn.on_press = self.save_and_continue

        # Добавяме бутона към оформлението.
        self.screen_layout.add_widget(btn)

            # Създаваме метод, който се изпълнява при натискане на бутона.
    def save_and_continue(self):

        # Взимаме въведеното име от полето и го записваме в речника.
        # Ключът 'name' ще се използва за достъп до името.
        results['name'] = self.name_input.text

        # Взимаме въведената възраст и я записваме в речника.
        # На този етап стойността се запазва като текст.
        results['age'] = self.age_input.text

        # Казваме на ScreenManager да покаже екрана с име 'second'.
        self.manager.current = 'second'

        # Отпечатваме двойките ключ-стойност от речника в конзолата.
        # Това ни позволява да проверим дали данните са запазени.
        print(results.items())

# Създаваме втория екран.
# Засега той е празен, защото класът няма допълнителна логика.
class SecondScreen(Screen):
    pass


# Създаваме третия екран.
class ThirdScreen(Screen):
    pass


# Създаваме четвъртия екран.
class FourthScreen(Screen):
    pass


# Създаваме петия екран.
class FifthScreen(Screen):
    pass


# Създаваме главния клас на приложението.
class RufferIndex(App):

    # Методът build създава интерфейса, който приложението ще покаже.
    def build(self):

        # Създаваме ScreenManager, който ще управлява петте екрана.
        sm = ScreenManager()

        # Създаваме първия екран и му задаваме име 'first'.
        sm.add_widget(FirstScreen(name='first'))

        # Добавяме втория екран с име 'second'.
        sm.add_widget(SecondScreen(name='second'))

        # Добавяме третия екран с име 'third'.
        sm.add_widget(ThirdScreen(name='third'))

        # Добавяме четвъртия екран с име 'fourth'.
        sm.add_widget(FourthScreen(name='fourth'))

        # Добавяме петия екран с име 'fifth'.
        sm.add_widget(FifthScreen(name='fifth'))

        # Връщаме ScreenManager, за да се покаже като интерфейс на приложението.
        return sm


# Създаваме обект на приложението.
app = RufferIndex()

# Стартираме приложението.
app.run()