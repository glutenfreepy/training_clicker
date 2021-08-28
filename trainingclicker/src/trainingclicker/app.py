"""
Click the 'Next' button of your boring training repeatedly
"""
import time
import toga

import pyautogui
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def TrainingClicker(toga.App):
    main_box = toga.Box(style=Pack(direction=COLUMN))
    divider = toga.Divider()

    step_one_label = toga.Label(
        'Step 1: First, pause your training video where we can see the Next button,\n'
        'Step 2: Next, we need to get the coordinates of the Next button,\n'
        '  - Click the button below to start the countdown,\n'
        '  - Then hover your mouse over the Next button for 5 seconds until coordinates are acquired\n',
        style=Pack(padding=(0, 5))
    )
    steps_box = toga.Box(style=Pack(direction=ROW, padding=5))
    steps_box.add(step_one_label)
    #steps_box.add(coord_label)

    def get_coords(widget):
        # TODO: display a countdown
        time.sleep(5)
        mouse_loc = pyautogui.position()
        print(mouse_loc)

    coord_button = toga.Button(
        'Get Next button coordinates',
        on_press=get_coords,
        style=Pack(padding=5)
    )
    #coord_label = toga.Label(f"Coordinates: {self.mouse_loc}")



    main_box.add(steps_box)
    main_box.add(coord_button)
    main_box.add(divider)

    # TODO: display mouse coords

    main_window = toga.MainWindow()
    main_window.content = main_box
    main_window.show()


def main():
    return TrainingClicker()
