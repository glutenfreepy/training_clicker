"""
Click the 'Next' button of your boring training repeatedly
"""
import time
import toga

import pyautogui
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class TrainingClicker(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))
        divider = toga.Divider()
        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        step_one_label = toga.Label(
            'Step 1: First, pause your training video where we can see the Next button,\n'
            'Step 2: Next, we need to get the coordinates of the Next button,\n'
            '  - Click the button below to start the countdown,\n'
            '  - Hold your mouse cursor over the Next button until the countdown ends\n',
            style=Pack(padding=(0, 5))
        )
        step_one_box = toga.Box(style=Pack(direction=ROW, padding=5))
        step_one_box.add(step_one_label)

        coord_button = toga.Button(
            'Get Next button coordinates',
            on_press=self.get_coords,
            style=Pack(padding=5)
        )

        main_box.add(step_one_box)
        main_box.add(divider)
        main_box.add(coord_button)
        main_box.add(divider)

        # TODO: display mouse coords

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def get_coords(self, widget):
        # TODO: display a countdown
        time.sleep(5)
        self.mouse_loc = pyautogui.position()
        print(self.mouse_loc)

    def say_hello(self, widget):
        """
        Pop up a window that says hello
        """
        name = self.name_input.value
        label = toga.Label(f'Hello, {name}')
        outer_box = toga.Box(
            children=[label]
        )
        window = toga.Window('id-window', title='Hi')
        window.content = outer_box
        window.show()


def main():
    return TrainingClicker()

