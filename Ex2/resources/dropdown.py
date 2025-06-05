from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class DropdownElement:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def switch_to_iframe(self):
        iframe = self.wait.until(
            ec.presence_of_element_located((By.XPATH, "//iframe[contains(@class, 'demo-module--demoFrame')]"))
        )
        self.driver.switch_to.frame(iframe)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def scroll_down(self):
        self.switch_to_iframe()

        example_element = self.wait.until(
            ec.presence_of_element_located((By.XPATH, "//*[@class='k-body']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", example_element)

        self.switch_to_default()

    def change_theme(self):
        self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='Change theme']"))
        ).click()
        self.wait.until(
            ec.element_to_be_clickable((By.XPATH, "//button[13]"))  # achieved by a browser extension SelectorsHub
        ).click()
        print("Successfully changed Material Theme to Main!")
