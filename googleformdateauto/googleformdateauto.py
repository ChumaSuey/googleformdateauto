#This selenium script goes to specified Google forms (in this case 3, in spanish)
#And it's function is just to pick today's date.
# Selenium - Python script by Chuma and Nepta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

#Used to be like 8 libraries but they were cleaned to 5

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#This Experimental function tells chrome to not close after finishing it (Selenium does it automatically)

today_date = datetime.today().strftime('%m/%d/%Y')

#Selenium 4.6+ automatically manages ChromeDriver - no manual path needed!
#It will download the correct version matching your Chrome browser automatically

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
#At this point it's important to specify the link of the form, it's the first and Chrome is opening, so key element to use .get
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSewqr62ef2zxsB_2ZS-jQHz6BRbv_kny52WIRZ82lESUPS7EQ/viewform?usp=sf_link")
window_before = driver.window_handles[0] #This is important, we have to declare the variable window_handles and it's position in array.
time.sleep(1)
date_input = driver.find_element(By.XPATH, "//input[@type='date']").send_keys(today_date)  #This will find by partial XPath the datepicker in the form
time.sleep(3)
#If it were just one google form, it would just go ahead and the script completed it's function
#For demonstration effects we will do it with 2 other forms i've created.

#it would be prudent to have a very small wait, and we've learned to not mix implicit waits and webdriver waits.

driver.implicitly_wait(10)

#The next script will just open a new window
driver.execute_script('window-open("https://docs.google.com/forms/d/e/1FAIpQLSeBmm5GJeKML_Oyi7hyhjof3vXl72ap5pvMFDD5nB-8kREP8g/viewform?usp=sf_link")')
#This is where it gets tricky: the variable will need to be declared so Selenium not only opens but Operates in the new window
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
#In the past 2 lines, The new window was declared in position 1, and the window has been switched.
time.sleep(1)
date_input = driver.find_element(By.XPATH, "//input[@type='date']").send_keys(today_date)
time.sleep(3)
window_before = driver.window_handles[1]

#The current window (window 2) was declared as the "old" window


#We will repeat the same step in the last page.
#So we would need to declare window handle [N] and a successor window that will be the new one in position [N+1]


driver.implicitly_wait(10)

driver.execute_script('window-open("https://docs.google.com/forms/d/e/1FAIpQLSfb6Xu4DRV4gbcw0DdvhC_QykN9O4pPzaotf2N1QMUY28-qaA/viewform?usp=sf_link")')
window_after = driver.window_handles[2]
driver.switch_to.window(window_after)
time.sleep(1)
date_input = driver.find_element(By.XPATH, "//input[@type='date']").send_keys(today_date)



#For more google forms, this portion of the code would need to be c&p , knowing the google form in advance.
#By Chuma (Software engineer, QA Manual, Automation enthusiast) and Nepta (Backend programmer, Automation guru and enthusiast)


#Cut import and code line:

#from selenium.webdriver.support.wait import WebDriverWait

#wait = WebDriverWait(driver, 30)

#This wasn't used properly but it tells the browser to wait certain time, it's an implicit wait

#Update march 13 2025 : Chrome Driver is being used locally and small line changes on its use
# gfdauto2.py is the script without any comments, just the code.
