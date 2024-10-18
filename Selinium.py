from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
import time

def submit_form(Name,Email):
     options=Options() 
     options.add_experimental_option("detach",True)

     driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options) 
     driver.get("https://tally.so/r/mDJgJX")
     driver.maximize_window()
     time.sleep(1)

#links=driver.find_elements("xpath","a//[@href]") 
     name_field = driver.find_element("xpath", "//input[@name='Name']")
     email_field = driver.find_element("xpath", "//input[@name='Email']")

     name_field.send_keys(Name)
     email_field.send_keys(Email)

     done_button = driver.find_element("xpath", "//button[text()='Done']")
     done_button.click()

time.sleep(2)