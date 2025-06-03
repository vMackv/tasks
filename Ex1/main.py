from Task1 import AutomateBrowser as AB

def RunBrowser():
    auto = AB()
    auto.Open_URL()
    auto.Reject_Cookies()
    auto.Swap_To_Iframe()
    auto.Scroll_Down()
    auto.Default_Frame()
    auto.Change_Theme()
    auto.Swap_To_Iframe()
    auto.Style_Underline()
    auto.Default_Frame()
    auto.Take_Screenshot()
    input('Press Enter to continue...')
    auto.Driver_quit()

if __name__ == '__main__':
    RunBrowser()
