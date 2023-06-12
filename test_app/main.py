from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp


class SalaryCalcLayout(BoxLayout):
    pass


class SalaryCalc(MDApp):
    def calculate(self, instance):
        try:
            tip_amount = int(self.root.ids.tip_amount.text)
            base_salary = int(self.root.ids.base_salary.text)
            result = (tip_amount - base_salary) * 0.25 + base_salary
            self.root.ids.result_label.text = f"Your salary is: {result}, company get {tip_amount - result}"
        except ValueError:
            self.root.ids.result_label.text = "Please enter integers"

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "A400"
        Builder.load_file('my2.kv')
        return SalaryCalcLayout()
        


if __name__ == '__main__':
    SalaryCalc().run()
