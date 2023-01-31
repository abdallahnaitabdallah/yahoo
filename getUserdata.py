from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

username = 'abdallah_nait'
pwd = 'Nait_abdallah592@'

def get_user_info(browser):
    
    user_info = {
        "firstname": str,
        "lastname": str,
        "phone": int
    }
    # return to tab with index 0 to genarate and get a user name 
    browser.switch_to.window(driver.window_handles[0])

    browser.find_element(By.ID,'genbtn').click()
    user = browser.find_element(By.CLASS_NAME,'address').find_element(By.TAG_NAME,'h3').text
    user = user.split(' ')
    del user[1]
    user_info["firstname"] = str(user[0])
    user_info["lastname"] = str(user[1])

    # return to tab with index 1 to select and get the phone number 
    browser.switch_to.window(browser.window_handles[1])
    
    selected_value = Select(browser.find_element(By.TAG_NAME,"select")).select_by_index(index)
    user_info["phone"] = element.get_attribute('value')
    
    return user_info

def get_validation_code(browser):
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element(By.TAG_NAME,"form").submit()
    
    
