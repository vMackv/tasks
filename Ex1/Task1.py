import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains

class AutomateBrowser:

    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)

        options = Options()
        service = Service(GeckoDriverManager().install())
        #options.headless = True
        self.driver = webdriver.Firefox(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)
        self.current_url = "https://www.telerik.com/kendo-react-ui/components/layout/contextmenu"

    def Open_URL(self):
        try:
            self.driver.get(self.current_url)
            print('Program running...')
            print('\nOpening the url: {}'.format(self.current_url))
        except Exception as e:
            print('Something went wrong: {}'.format(e))

    def Reject_Cookies(self):
        try:
            reject = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reject All')]"))
            )
            self.driver.execute_script('arguments[0].click();', reject)
            print('Cookies rejected successfully.')
        except NoSuchElementException:
            print('Cookies not found.')

    def Swap_To_Iframe(self):
        try:
            iframe = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//iframe[contains(@class, 'demo-module--demoFrame')]"))
            )
            self.driver.switch_to.frame(iframe)
        except NoSuchElementException:
            print('No iframe found.')

    def Default_Frame(self):
        try:
            self.driver.switch_to.default_content()
        except NoSuchElementException:
            print('Default frame actually enabled.')

    def Scroll_Down(self):
        try:
            example_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[@class='k-body']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", example_element)
            print("Scrolled down successfully!")
        except NoSuchElementException:
            print('Example element not found.')
        except Exception as e:
            print('Error scrolling down: {}'.format(e))

    def Change_Theme(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Change theme']"))
            ).click()
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[13]"))  # achieved by a browser extension SelectorsHub
            ).click()
            print("Successfully changed Material Theme to Main!")
        except NoSuchElementException:
            print('Dropdown button not found.')
        except Exception as e:
            print('Error clicking material theme: {}'.format(e))

    def Style_Underline(self):
        try:
            rc_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='target']"))
            )
            self.actions.context_click(rc_button).perform()
            style_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Style']"))
            )
            self.actions.move_to_element(style_btn).perform()
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[text()='Underline']"))
            ).click()
            print("Clicked underline button!")
        except Exception as e:
            print('Error changing button style: {}'.format(e))

    def Take_Screenshot(self):
        try:
            script_dir = os.path.dirname(__file__)
            os.chdir(script_dir)
            time.sleep(1)

            screenshot = self.driver.save_screenshot('whole_website.png')

            if screenshot:
                print("Successfully taken screenshot!")
            else:
                print('Could not take screenshot!')
        except Exception as e:
            print('Error taking screenshot: {}'.format(e))

    def Driver_quit(self):
        try:
            self.driver.quit()
            print('Driver closed successfully.')
        except Exception as e:
            print('Error quiting driver: {}'.format(e))