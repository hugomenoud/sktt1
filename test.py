import pyautogui
import os
import time

round_region = (100, 100, 200, 50)  # Adjust the coordinates and size according to your screen

# Set the directory to save the screenshots
screenshot_dir = 'tft_screenshots'

# Create the screenshot directory if it doesn't exist
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

previous_round = None

round_screenshot = pyautogui.screenshot(region=round_region)

timestamp = time.strftime("%Y%m%d_%H%M%S")
screenshot_path = os.path.join(screenshot_dir, f'tft_round_"current_round"_{timestamp}.png')
round_screenshot.save(screenshot_path)
