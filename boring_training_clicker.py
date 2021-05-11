import pyautogui

# get mouse coordinates
print("First we need to know where the 'Next' button of your video is.")
print("Please hold your mouse over the 'Next' button of the boring video.")
input("Press Enter when ready")

# do a countdown here
# 3
# 2
# 1
mouse_loc = pyautogui.position()
clicks = 1000
interval = 10
button = 'left'

# send mouse to coordinates
pyautogui.moveTo(mouse_loc)

# instead we can use click() to go to the coords before clicking
# call click funtion to click next on the video and advance the lesson slide
pyautogui.click(clicks=clicks, interval=interval, button=button)

print('pyautogui process is complete')
#prompt to run again
