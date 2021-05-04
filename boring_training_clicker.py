import pyautogui

# get mouse coordinates
print("First we need to know where the 'Next' button of your video is.")
print("Please hold your mouse over the 'Next' button of the boring video.")
mouse_loc = pyautogui.position()

# send mouse to coordinates
 pyautogui.moveTo(mouse_loc)

# instead we can use click() to go to the coords before clicking
# call click funtion to click next on the video and advance the lesson slide
pyautogui.click(clicks=100, interval=10, button='left')

print('pyautogui process is complete')


