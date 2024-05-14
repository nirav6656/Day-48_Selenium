from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

first_name = driver.find_element(By.ID, "cookie")
for i in range(50):
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
    time.sleep(1)
money = int(driver.find_element(By.ID,"money").text)
def cookie():
    for i in reversed(range(0,8)):
        count = int(driver.find_elements(By.CSS_SELECTOR,"#store b")[i].text.split(" ")[-1].replace(",",""))
        if money > count:
            driver.find_element(By.CSS_SELECTOR,"#store b").click()


timeout = time.time() + 60*5    # 5 minutes from now
while True:
    test = 0
    cookie()
    if test == 5 or time.time() > timeout:
        break
    test = test - 1

driver.quit()