import time
from Task1 import AutomateBrowser as ab

def RunBrowser():
    auto = ab()
    auto.open_url()
    auto.reject_cookies()
    auto.swap_to_iframe()
    auto.scroll_down()
    auto.default_frame()
    auto.change_theme()
    auto.swap_to_iframe()
    auto.style_underline()
    auto.default_frame()
    auto.take_screenshot()
    #input('Press Enter to continue...')
    time.sleep(2)
    auto.driver_quit()

if __name__ == '__main__':
    RunBrowser()
