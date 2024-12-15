import pyautogui
from PIL import ImageGrab
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DinoBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.game_link = "https://chromedino.com/"
        self.delay = 5
        self.pixel_black_threshold = 100
        self.detection_area = (750, 480, 835, 595)

    def hit(self, key):
        pyautogui.press(key)

    def is_collide(self, data):
        left, top, right, bottom = self.detection_area
        for x in range(left, right):
            for y in range(top, bottom):
                if data[x, y] < self.pixel_black_threshold:
                    self.hit("up")
                    return True
        return False

    def main(self):
        try:
            self.driver.get(self.game_link)
            self.driver.maximize_window()
            time.sleep(self.delay)
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SPACE)

            while True:
                if len(self.driver.window_handles) == 0:
                    break
                image = ImageGrab.grab().convert('L')
                data = image.load()
                self.is_collide(data)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.driver.quit()
'''
bot = DinoBot()
bot.main()
'''
