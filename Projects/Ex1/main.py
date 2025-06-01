from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


options = Options()
options.add_argument('-start-maximized')
options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
#options.add_argument('--headless')
service = Service('C:\\Users\\mszpa\\geckodriver.exe')

driver = webdriver.Firefox(service=service, options=options)

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

    input("Press enter to continue...")
except Exception as e:
    print(e)
finally:
    driver.quit()
