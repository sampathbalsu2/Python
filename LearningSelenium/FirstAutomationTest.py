import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://google.com")
print(driver.title)
driver.maximize_window()
time.sleep(2)
#driver.find_element(By.id,)
driver.quit()
