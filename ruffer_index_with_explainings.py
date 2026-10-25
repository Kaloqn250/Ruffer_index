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
# Създаваме клас за втория екран.
class SecondScreen(Screen):

    # Методът се изпълнява при създаването на екрана.
    def __init__(self, **kw):

        # Извикваме конструктора на родителския клас Screen.
        super().__init__(**kw)

        # Създаваме FloatLayout, в който ще поставим елементите.
        layout = FloatLayout()

        # Създаваме Label с инструкции към потребителя.
        text1 = Label(
            text='Mesure your pulse for 15 seconds \n'
                 'Write the result in the box bellow.',

            # Поставяме текста в центъра на екрана.
            pos_hint={
                'center_x': 0.5,
                'center_y': 0.5
            }
        )

        # Създаваме Label, който указва какво трябва да се въведе.
        text2 = Label(
            text='Enter the result: ',
            pos_hint={
                'center_x': 0.3,
                'center_y': 0.3
            }
        )

        # Създаваме поле за въвеждане на първия резултат от измерването.
        self.pulse_input = TextInput(
            size_hint=(0.3, 0.05),
            pos_hint={
                'center_x': 0.6,
                'center_y': 0.3
            }
        )

        # Създаваме бутон за преминаване към следващия екран.
        btn = Button(
            text='Continue',
            size_hint=(0.3, 0.15),
            pos_hint={
                'center_x': 0.5,
                'center_y': 0.1
            }
        )

        # Свързваме бутона с метода, който запазва резултата
        # и отваря третия екран.
        btn.on_press = self.save_and_continue

        # Добавяме всички елементи към оформлението.
        layout.add_widget(text1)
        layout.add_widget(text2)
        layout.add_widget(self.pulse_input)
        layout.add_widget(btn)

        # Добавяме цялото оформление към текущия екран.
        self.add_widget(layout)

    # Методът се изпълнява при натискане на бутона.
    def save_and_continue(self):

        # Взимаме въведения текст от полето и го запазваме
        # в общия речник results под ключа 'first_measure'.
        results['first_measure'] = self.pulse_input.text

        # Преминаваме към екрана с име 'third'.
        self.manager.current = 'third'


# Създаваме третия екран.
# Създаваме клас за третия екран.
class ThirdScreen(Screen):

    def __init__(self, **kw):

        # Извикваме конструктора на Screen.
        super().__init__(**kw)

        # Създаваме оформление за елементите.
        layout = FloatLayout()

        # Показваме инструкция за изпълнение на физическото упражнение.
        label = Label(text='Do 30 squats in 45 seconds')

        # Създаваме бутон за продължаване.
        btn = Button(
            text='Continue',
            size_hint=(0.3, 0.15),
            pos_hint={
                'center_x': 0.5,
                'center_y': 0.1
            }
        )

        # При натискане на бутона ще се извика методът btn_continue.
        btn.on_press = self.btn_continue

        # Добавяме текста и бутона към оформлението.
        layout.add_widget(label)
        layout.add_widget(btn)

        # Добавяме оформлението към екрана.
        self.add_widget(layout)

    # Метод за преминаване към четвъртия екран.
    def btn_continue(self):

        # Показваме екрана с име 'fourth'.
        self.manager.current = 'fourth'

#00000
# Създаваме четвъртия екран.
# Създаваме клас за четвъртия екран.
class FourthScreen(Screen):

    def __init__(self, **kw):

        # Извикваме конструктора на родителския клас.
        super().__init__(**kw)

        # Създаваме оформление за елементите.
        layout = FloatLayout()

        # Създаваме текст с инструкции за двете измервания.
        text = Label(
            text='Measure your pulse twice in the next minute \n'
                 'during the first 15 seconds, and in the last 15 seconds \n'
                 'Write the results below'
        )

        # Създаваме етикет за първото измерване след кляканията.
        result_1 = Label(
            text='First result: ',
            pos_hint={
                'center_x': 0.25,
                'center_y': 0.35
            }
        )

        # Създаваме етикет за второто измерване след кляканията.
        result_2 = Label(
            text='Second result: ',
            pos_hint={
                'center_x': 0.25,
                'center_y': 0.25
            }
        )

        # Създаваме поле за въвеждане на първия резултат.
        self.res_1_input = TextInput(
            size_hint=(0.3, 0.05),
            pos_hint={
                'center_x': 0.6,
                'center_y': 0.35
            }
        )

        # Създаваме поле за въвеждане на втория резултат.
        self.res_2_input = TextInput(
            size_hint=(0.3, 0.05),
            pos_hint={
                'center_x': 0.6,
                'center_y': 0.25
            }
        )

        # Създаваме бутон за преминаване към последния екран.
        btn = Button(
            text='Continue',
            size_hint=(0.3, 0.15),
            pos_hint={
                'center_x': 0.5,
                'center_y': 0.1
            }
        )

        # Свързваме бутона с метода за запазване на резултатите.
        btn.on_press = self.save_and_continue

        # Добавяме елементите към оформлението.
        layout.add_widget(text)
        layout.add_widget(result_1)
        layout.add_widget(result_2)
        layout.add_widget(self.res_1_input)
        layout.add_widget(self.res_2_input)
        layout.add_widget(btn)

        # Добавяме оформлението към екрана.
        self.add_widget(layout)

    # Метод, който се изпълнява при натискане на бутона.
    def save_and_continue(self):

        # Запазваме първия резултат в общия речник.
        results['second_measure'] = self.res_1_input.text

        # Запазваме втория резултат в общия речник.
        results['third_measure'] = self.res_2_input.text

        # Извеждаме всички запазени данни в конзолата.
        print(results.items())

        # Преминаваме към петия екран.
        self.manager.current = 'fifth'


# Създаваме петия екран.
# Създаваме клас за петия екран.
class FifthScreen(Screen):

    def __init__(self, **kw):

        # Извикваме конструктора на Screen.
        super().__init__(**kw)

        # Създаваме оформление за резултатите.
        layout = FloatLayout()

        # Създаваме празен Label, в който по-късно ще покажем резултата.
        self.result_label = Label(text='')

        # Добавяме етикета към оформлението.
        layout.add_widget(self.result_label)

        # Добавяме оформлението към екрана.
        self.add_widget(layout)

    # Този метод се извиква непосредствено преди показването на екрана.
    def on_pre_enter(self, *args):

        # Извикваме метода, който изчислява и показва резултатите.
        self.show_results()

    # Метод за изчисляване на индекса и показване на информацията.
    def show_results(self):

        # Взимаме първото измерване от речника и го преобразуваме
        # от текст в цяло число.
        p1 = int(results['first_measure'])

        # Взимаме второто измерване и го преобразуваме в цяло число.
        p2 = int(results['second_measure'])

        # Взимаме третото измерване и го преобразуваме в цяло число.
        p3 = int(results['third_measure'])

        # Изчисляваме индекса на Руфие по формулата.
        index = (4 * (p1 + p2 + p3) - 200) / 10

        # Създаваме празен текст, в който ще запишем оценката.
        text = ''

        # Проверяваме стойността на индекса.
        if index <= 3:
            text = 'Perfect condition'

        # Ако първото условие не е изпълнено, проверяваме следващото.
        elif index <= 6:
            text = 'Good condition'

        # Проверяваме дали индексът е до 9.
        elif index <= 9:
            text = 'Not the best you can have'

        # Проверяваме дали индексът е до 14.
        elif index <= 14:
            text = 'Not very good condition'

        # Ако никое от горните условия не е изпълнено.
        else:
            text = 'Go to see a doctor'

        # Показваме името, възрастта и оценката в Label.
        self.result_label.text = (
            f"Name: {results.get('name')}\n"
            f"Age: {results['age']}\n"
            f"Ruffier Index: {index:.2f}\n"
            f"Result from the test: {text}"
        )


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
