from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import sympy as sp

# Background color aapke design jaisa
Window.clearcolor = get_color_from_hex('#AFB7BA')

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # Display Area
        self.display = Label(
            text="0", font_size='40sp', halign='right', valign='middle',
            size_hint=(1, 0.25), color=get_color_from_hex('#2C3E50'),
            text_size=(Window.width - 50, None)
        )
        
        with self.display.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(209/255, 217/255, 217/255, 1)
            self.rect = Rectangle(size=self.display.size, pos=self.display.pos)
        self.display.bind(size=self._update_rect, pos=self._update_rect)
        
        root.add_widget(self.display)

        # Buttons Grid
        grid = GridLayout(cols=5, spacing=5)
        btn_labels = [
            ['Abs', 'x³', 'xⁿ', 'log', 'ln'],
            ['(', ')', 'sin', 'cos', 'tan'],
            ['7', '8', '9', 'DEL', 'AC'],
            ['4', '5', '6', '×', '÷'],
            ['1', '2', '3', '+', '-'],
            ['0', '.', 'π', 'e', '=']
        ]

        for row in btn_labels:
            for label in row:
                bg_c = '#E5E7E9'
                txt_c = '#1B4F72'
                if label.isdigit() or label == '.': bg_c = '#FDFEFE'; txt_c = '#17202A'
                elif label in ['DEL', 'AC']: bg_c = '#EB984E'; txt_c = '#FFFFFF'
                elif label == '=': bg_c = '#52BE80'; txt_c = '#FFFFFF'

                btn = Button(text=label, font_size='18sp', bold=True,
                             background_normal='', background_color=get_color_from_hex(bg_c),
                             color=get_color_from_hex(txt_c))
                btn.bind(on_press=self.on_click)
                grid.add_widget(btn)

        root.add_widget(grid)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_click(self, instance):
        v = instance.text
        if v == "AC": self.expression = ""
        elif v == "DEL": self.expression = self.expression[:-1]
        elif v == "=":
            try:
                p = self.expression.replace('×', '*').replace('÷', '/').replace('π', 'pi').replace('x³', '**3').replace('xⁿ', '**')
                self.expression = str(round(float(sp.sympify(p).evalf()), 4))
            except: self.expression = "Error"
        else: self.expression += v
        self.display.text = self.expression if self.expression else "0"

if __name__ == "__main__":
    CalculatorApp().run()