from Task1 import AutomateBrowser
from resources.dropdown import DropdownElement
from resources.context_menu import ContextMenu

class CustomLibrary:

    def __init__(self, headless=False):
        self._browser = None
        self.headless = headless

    # Properties
    @property
    def keywords(self):
        if self._browser is None:
            self._browser = AutomateBrowser(headless=self.headless)
        return self._browser

    def open_url(self):
        self.keywords.open_url()

    def reject_cookies(self):
        self.keywords.reject_cookies()

    def change_theme(self):
        dropdown = DropdownElement(self.keywords.driver, self.keywords.wait)
        dropdown.change_theme()

    def style_underline(self):
        context_menu = ContextMenu(self.keywords.driver, self.keywords.wait, self.keywords.actions)
        context_menu.underline_text()

    def take_screenshot(self):
        self.keywords.take_screenshot()

    def close_browser(self):
        self.keywords.driver_quit()
