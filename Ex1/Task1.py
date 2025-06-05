import time
import shutil
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class AutomateBrowser:

    def __init__(self):
        options = Options()

        # Find the path to the Firefox browser
        firefox_path = shutil.which('firefox')
        if not firefox_path:
            raise FileNotFoundError('Firefox not found in PATH.')
        options.binary_location = firefox_path

        # Find the path to the geckodriver
        geckodriver_path = shutil.which('geckodriver')
        if not geckodriver_path:
            raise FileNotFoundError('geckodriver not found in PATH.')
        service = Service(geckodriver_path)

        #options.headless = True
        # Launch Firefox browser with specified options
        self.driver = webdriver.Firefox(service=service, options=options)

        # Used for waiting for elements to appear
        self.wait = WebDriverWait(self.driver, 10)

        # Used for mouse actions like right-click
        self.actions = ActionChains(self.driver)

        # URL to open in Firefox browser
        self.current_url = "https://www.telerik.com/kendo-react-ui/components/layout/contextmenu"

    # Open the URL in Firefox browser
    def open_url(self):
        try:
            self.driver.get(self.current_url)
            print('Program running...')
            print('\nOpening the url: {}'.format(self.current_url))
        except Exception as e:
            print('Something went wrong: {}'.format(e))

    # Reject the cookie pop-up if it appears
    def reject_cookies(self):
        try:
            reject = self.wait.until(
                ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reject All')]"))
            )
            self.driver.execute_script('arguments[0].click();', reject)
            print('Cookies rejected successfully.')
        except NoSuchElementException:
            print('Cookies not found.')

    # Switch into an iframe
    def swap_to_iframe(self):
        try:
            iframe = self.wait.until(
                ec.presence_of_element_located((By.XPATH, "//iframe[contains(@class, 'demo-module--demoFrame')]"))
            )
            self.driver.switch_to.frame(iframe)
        except NoSuchElementException:
            print('No iframe found.')

    # Switch back to the default page frame
    def default_frame(self):
        try:
            self.driver.switch_to.default_content()
        except NoSuchElementException:
            print('Default frame actually enabled.')

    # Scroll down to a specific element
    def scroll_down(self):
        try:
            example_element = self.wait.until(
                ec.presence_of_element_located((By.XPATH, "//*[@class='k-body']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", example_element)
            print("Scrolled down successfully!")
        except NoSuchElementException:
            print('Example element not found.')
        except Exception as e:
            print('Error scrolling down: {}'.format(e))

    # Change the UI theme on the page
    def change_theme(self):
        try:
            self.wait.until(
                ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='Change theme']"))
            ).click()
            self.wait.until(
                ec.element_to_be_clickable((By.XPATH, "//button[13]"))  # achieved by a browser extension SelectorsHub
            ).click()
            print("Successfully changed Material Theme to Main!")
        except NoSuchElementException:
            print('Dropdown button not found.')
        except Exception as e:
            print('Error clicking material theme: {}'.format(e))

    # Right-click on a target element and select "Underline" style
    def style_underline(self):
        try:
            rc_button = self.wait.until(
                ec.presence_of_element_located((By.XPATH, "//div[@class='target']"))
            )
            self.actions.context_click(rc_button).perform()
            style_btn = self.wait.until(
                ec.element_to_be_clickable((By.XPATH, "//*[text()='Style']"))
            )
            self.actions.move_to_element(style_btn).perform()
            self.wait.until(
                ec.element_to_be_clickable((By.XPATH, "//*[text()='Underline']"))
            ).click()
            print("Clicked underline button!")
        except Exception as e:
            print('Error changing button style: {}'.format(e))

    # Take a screenshot of the entire page
    def take_screenshot(self):
        try:
            time.sleep(1)
            screenshot = self.driver.save_screenshot('whole_website.png')

            if screenshot:
                print("Successfully taken screenshot!")
            else:
                print('Could not take screenshot!')
        except Exception as e:
            print('Error taking screenshot: {}'.format(e))

    # Close the browser window
    def driver_quit(self):
        try:
            self.driver.quit()
            print('Driver closed successfully.')
        except Exception as e:
            print('Error quiting driver: {}'.format(e))