import kivy
import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Tuile(Button):
    def __init__(self, couleur, **kwargs):
        super(Tuile, self).__init__(**kwargs)
        self.couleur = couleur
        self.background_color = couleur

class Tableau(GridLayout):
    def __init__(self, **kwargs):
        super(Tableau, self).__init__(**kwargs)
        self.cols = 5
        self.rows = 5
        self.tuiles = []
        for i in range(25):
            tuile = Tuile(couleur=(random.random(), random.random(), random.random(), 1))
            self.add_widget(tuile)
            self.tuiles.append(tuile)

class CandyCrushApp(App):
    def build(self):
        return Tableau()

if __name__ == '__main__':
    CandyCrushApp().run()