from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp, App
from kivy.uix.screenmanager import ScreenManager, Screen


class SunsetTour(Screen):
    def calculate(self, instance):
        try:
            tip_amount = int(self.ids.tip_amount.text)
            base_salary = int(self.ids.base_salary.text)
            result = ((tip_amount - base_salary) * 0.3) + base_salary
            self.ids.result_label.text = f"Your salary is: {result}, company gets {tip_amount - result}"
        except ValueError:
            self.ids.result_label.text = "Please enter integers"


class MenuScreen(Screen):
    pass

class IntroTour(Screen):
    def calculate(self, instance):
        try:
            tip_amount = int(self.ids.tip_amount.text)
            base_salary = int(self.ids.base_salary.text)
            result = (tip_amount - base_salary) * 0.25 + base_salary
            self.ids.result_label.text = f"Your salary is: {result}, company gets {tip_amount - result}"
        except ValueError:
            self.ids.result_label.text = "Please enter integers"


class SalaryCalc(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "300"
        Builder.load_file('my2.kv')
        # # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(IntroTour(name='IntroTour'))
        sm.add_widget(SunsetTour(name='SunsetTour'))

        return sm
        


if __name__ == '__main__':
    SalaryCalc().run()
