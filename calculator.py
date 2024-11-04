from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp

# Define the KV layout for the calculator
kv = '''
Screen:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        MDLabel:
            text: "Simple Calculator"
            halign: 'center'
            font_style: 'H4'

        TextInput:
            id: calc_input
            hint_text: "0"
            halign: "right"
            font_size: 32
            multiline: False
            readonly: True
            size_hint_y: None
            height: dp(50)

        MDBoxLayout:
            spacing: dp(10)
            MDRaisedButton:
                text: "C"
                on_release: app.clear()
            MDRaisedButton:
                text: "←"
                on_release: app.backspace()
            MDRaisedButton:
                text: "/"
                on_release: app.add_operator("/")
            MDRaisedButton:
                text: "*"
                on_release: app.add_operator("*")

        MDBoxLayout:
            spacing: dp(10)
            MDRaisedButton:
                text: "7"
                on_release: app.add_number("7")
            MDRaisedButton:
                text: "8"
                on_release: app.add_number("8")
            MDRaisedButton:
                text: "9"
                on_release: app.add_number("9")
            MDRaisedButton:
                text: "-"
                on_release: app.add_operator("-")

        MDBoxLayout:
            spacing: dp(10)
            MDRaisedButton:
                text: "4"
                on_release: app.add_number("4")
            MDRaisedButton:
                text: "5"
                on_release: app.add_number("5")
            MDRaisedButton:
                text: "6"
                on_release: app.add_number("6")
            MDRaisedButton:
                text: "+"
                on_release: app.add_operator("+")

        MDBoxLayout:
            spacing: dp(10)
            MDRaisedButton:
                text: "1"
                on_release: app.add_number("1")
            MDRaisedButton:
                text: "2"
                on_release: app.add_number("2")
            MDRaisedButton:
                text: "3"
                on_release: app.add_number("3")
            MDRaisedButton:
                text: "="
                on_release: app.calculate()

        MDBoxLayout:
            spacing: dp(10)
            MDRaisedButton:
                text: "0"
                size_hint_x: 2
                on_release: app.add_number("0")
            MDRaisedButton:
                text: "."
                on_release: app.add_operator(".")
'''


class CalculatorApp(MDApp):
    def build(self):
        self.title = "Calculator"
        return Builder.load_string(kv)

    def add_number(self, number):
        """Appends a number to the current input."""
        current_text = self.root.ids.calc_input.text
        if current_text == "0":
            self.root.ids.calc_input.text = number
        else:
            self.root.ids.calc_input.text += number

    def add_operator(self, operator):
        """Appends an operator to the current input."""
        current_text = self.root.ids.calc_input.text
        # Prevent adding multiple operators or invalid sequences
        if current_text and current_text[-1] not in "+-*/.":
            self.root.ids.calc_input.text += operator

    def clear(self):
        """Clears the input field."""
        self.root.ids.calc_input.text = "0"

    def backspace(self):
        """Removes the last character from the input."""
        current_text = self.root.ids.calc_input.text
        if len(current_text) > 1:
            self.root.ids.calc_input.text = current_text[:-1]
        else:
            self.root.ids.calc_input.text = "0"

    def calculate(self):
        """Evaluates the expression in the input field."""
        current_text = self.root.ids.calc_input.text
        try:
            # Use eval() cautiously; only trusted input should be evaluated
            result = str(eval(current_text))
            self.root.ids.calc_input.text = result
        except Exception:
            self.root.ids.calc_input.text = "Error"


CalculatorApp().run()
