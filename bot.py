from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Monkey:
    def __init__(self,delay):
        self.driver = webdriver.Chrome()
        self.speed=delay
        self.count=0
        self.bot_link="https://monkeytype.com"

    def run_bot(self):
        self.driver.get(self.bot_link)
        try:
            self.driver.execute_script(
                'arguments[0].click()',
                self.driver.find_element(By.XPATH, '//*[@id="cookiesModal"]/div[2]/div[2]/div[2]/button[1]')
            )
            time.sleep(5)
            input_field = self.driver.switch_to.active_element
            while True:
                if len(self.driver.window_handles) == 0:
                    break
                word_elements = self.driver.find_elements(By.CSS_SELECTOR, "#words .word")

                for word_element in word_elements:
                    try:
                        word = word_element.text.strip()
                        print(f"Typing: '{word}'")
                        input_field.send_keys(word)
                        input_field.send_keys(Keys.SPACE)
                        self.count+=1
                        time.sleep(self.speed)
                    except Exception as e:
                        print(f"Error typing word: {e}")
                        continue

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            time.sleep(1)
            print(f"Words Per Minute: {2*self.count}")
            self.driver.quit()


