# selenium 

from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver="C:/Users/wasi_/Downloads/chromedriver_win32/chromedriver.exe"

driver=webdriver.Chrome(executable_path=chromedriver)
driver.get("https://wrehman.in")
elem = driver.find_element(By.ID, "menu-item-49")
print(elem.text)
driver.close()
driver.quit()