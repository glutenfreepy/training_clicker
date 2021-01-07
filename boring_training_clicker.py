# use pyautogui to click next every 10 seconds to get thru stupid lessons

# dont for get to activate virtualenv

import pyautogui

# get mouse coordinates of the next button on the screen
# prompt user to place the mouse on the next button
# get mouse x and y coords with
# pyautogui.position()

# send mouse to coordinates
# pyautogui.moveTo(184, 787)

# instead we can use click() to go to the coords before clicking
# call click funtion to click next on the video and advance the lesson slide
pyautogui.click(x=184, y=787, clicks=100, interval=10, button='left')

print('pyautogui process is complete')


