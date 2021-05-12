import pyautogui

# get mouse coordinates
print("***************************************************")
print("            Boring Training Clicker")
print("***************************************************")
print("First, pause your training video where we can see the Next button.")
print("Next, we need to get the coordinates of the 'Next' button.")
print("Keeping this window as the active window, and")
print("hold your mouse over the 'Next' button of the boring video.")
input("Press the Enter when ready")

mouse_loc = pyautogui.position()

print(f"Mouse pointer coordinates acquired at: {mouse_loc}")
# TODO: ask if necessary to get coords again
input("Press Enter to let me start clicking through your training!")
print("Proceeding")
print("The mouse will now be moved to the Next button's coordinates")
print("and clicked every 10 seconds, 1000 times")
print("press Ctrl-c to cancel")

clicks = 1000
interval = 10
button = 'left'

pyautogui.moveTo(mouse_loc)
pyautogui.click(clicks=clicks, interval=interval, button=button)

print('TrainingClicker process is complete')
# TODO: prompt to run again
