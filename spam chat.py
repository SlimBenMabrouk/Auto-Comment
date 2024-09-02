from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.profile = r"C:\Users\slim2\AppData\Roaming\Mozilla\Firefox\Profiles\o87j60co.default-release"
driver = webdriver.Firefox(options=options)
try:
    driver.get("https://exemple.com")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'chat-input'))
    )

    while True:
        time.sleep(3)  # Wait for 3 seconds for manual tasks

        input_chat = driver.find_element(By.CLASS_NAME, 'chat-input')
        input_chat.clear()  # Clear any previous text
        input_chat.send_keys('xd')

        chat_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='inner-label' and text()='Chat']"))
        )
        chat_button.click()

        time.sleep(60)  # Sleep for 1 minute and 2 seconds

except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    driver.quit()
