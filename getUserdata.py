from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

username = 'abdallah_nait'
pwd = 'Nait_abdallah592@'
drive = webdriver.Firefox()
def get_user_info():
    drive.get('https://www.fakenamegenerator.com/gen-random-us-uk.php')
    drive.find_element(By.ID,'genbtn').click()
    user = drive.find_element(By.CLASS_NAME,'address').find_element(By.TAG_NAME,'h3').text
    user = user.split(' ')
    del user[1]
    return user

def get_phone_number():
    drive.get("https://vsimcard.com/login.php")
    drive.find_element(By.NAME,"username").send_keys(username)
    sleep(1)
    drive.find_element(By.NAME,"password").send_keys(pwd)
    sleep(1)
    drive.find_element(By.TAG_NAME,"form").submit()
    sleep(5)
#    drive.get("https://vsimcard.com/member.php")
#    selected_value = Select(drive.find_element(By.TAG_NAME,"select")).select_by_index(index)
    options = [x for x in drive.find_element(By.TAG_NAME,"select").find_element(By.TAG_NAME,"option")]
    print(options)


def get_validation_code():
    drive.find_element(By.TAG_NAME,"form").submit()

get_phone_number()