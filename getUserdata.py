from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

username = 'abdallah_nait'
pwd = 'Nait_abdallah592@'

def get_user_info(driver):
    user_info = {
        "username": "",
        "phone": ""
    }
    driver.switch_to.window(driver.window_handles[0])

    driver.find_element(By.ID,'genbtn').click()
    user = driver.find_element(By.CLASS_NAME,'address').find_element(By.TAG_NAME,'h3').text
    user = user.split(' ')
    del user[1]
    user_info["username"] = user
    
    # open new tab and point on it 
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    
    selected_value = Select(driver.find_element(By.TAG_NAME,"select")).select_by_index(index)
    options = [x for x in driver.find_element(By.TAG_NAME,"select").find_element(By.TAG_NAME,"option")]
    
    return user_info

def get_validation_code(driver):
    driver.switch_to.window(driver.window_handles[1])
    drive.find_element(By.TAG_NAME,"form").submit()
