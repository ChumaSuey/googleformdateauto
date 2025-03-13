from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

today_date = datetime.today().strftime('%m/%d/%Y')
driver_path = "C:\\chromedriver\\chromedriver.exe"  # Ensure this path is correct
service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSewqr62ef2zxsB_2ZS-jQHz6BRbv_kny52WIRZ82lESUPS7EQ/viewform?usp=sf_link")
window_before = driver.window_handles[0]
time.sleep(1)
date_input = driver.find_element(By.XPATH, "//input[@type='date']").send_keys(today_date)
time.sleep(3)

driver.implicitly_wait(10)

driver.execute_script('window.open("https://docs.google.com/forms/d/e/1FAIpQLSeBmm5GJeKML_Oyi7hyhjof3vXl72ap5pvMFDD5nB-8kREP8g/viewform?usp=sf_link")')
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
time.sleep(1)
date_input = driver.find_element(By.XPATH, "//input[@type='date']").send_keys(today_date)
time.sleep(3)
window_before = driver.window_handles[1]

driver.implicitly_wait(10)

driver.execute_script('window.open("https://docs.google.com/forms/d/e/1FAIpQLSfb6Xu4DRV4gbcw0DdvhC_QykN9O4pPzaotf2N1QMUY28-qaA/viewform?usp=sf_link")')
window_after = driver.window_handles[2]
driver.switch_to.window(window_after)
time.sleep(1)
date_input = driver.find_element(By.XPATH, "//input[@type='date']").send_keys(today_date)