from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config


class KeyboardLayout(GridLayout):
    def __init__(self, **kwargs):
        super(KeyboardLayout, self).__init__(**kwargs)
        self.cols = 3
        self.spacing = [5, 5]

        keys = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["C", "0", "OK"]
        ]

        for row in range(4):
            for col in range(3):
                key = keys[row][col]
                button = Button(text=key, font_size=20)
                button.bind(on_release=lambda btn: self.on_keypress(btn.text))
                self.add_widget(button)

    def on_keypress(self, key):
        print(f"Hai premuto il tasto: {key}")


class KeyboardApp(App):
    def build(self):
        Config.set('graphics', 'width', '400')
        Config.set('graphics', 'height', '400')
        return KeyboardLayout()


if __name__ == '__main__':
    KeyboardApp().run()
