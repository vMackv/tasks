from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class ContextMenu:

    def __init__(self, driver, wait, actions):
        self.driver = driver
        self.wait = wait
        self.actions = actions

    def switch_to_iframe(self):
        iframe = self.wait.until(
            ec.presence_of_element_located((By.XPATH, "//iframe[contains(@class, 'demo-module--demoFrame')]"))
        )
        self.driver.switch_to.frame(iframe)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def underline_text(self):
        self.switch_to_iframe()

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

        self.switch_to_default()