from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('-start-maximized')
#options.add_argument('--headless')

options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe" # pass your own firefox.exe path
service = Service('C:\\Users\\mszpa\\geckodriver.exe') # pass your own geckodriver.exe path

driver = webdriver.Firefox(service=service, options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.telerik.com/kendo-react-ui/components/layout/contextmenu")

    try:
        reject_cookie = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Reject All']"))
        )
        driver.execute_script("arguments[0].click();", reject_cookie)
        print("Rejected cookies successfully!")
    except Exception as e:
        print("Error rejecting cookies: ", e)

    try:
        iframe = wait.until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@class, 'demo-module--demoFrame')]"))
        )
        driver.switch_to.frame(iframe)
        print("Successfully switched to iframe!")
    except Exception as e:
        print("Error finding iframe: ", e)

    try:
        example_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='k-body']"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", example_element)
        print("Scrolled down successfully!")
    except Exception as e:
        print("Error scrolling down: ", e)

    input("Press enter to continue...")
except Exception as e:
    print(e)
finally:
    driver.quit()
