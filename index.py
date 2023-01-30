from selenium import webdriver
from selenium.webdriver.common.by import By
#set proxy import 
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from getUserdata import get_phone_number,get_user_info,get_validation_code
# manage time sleep 
from time import sleep


DATA = {
    "url":str,
    "field":{
        'first_name':str,
        'last_name':str,
        'email':str,
        'password':str,
        'year_of_birth':int,
        'phone_number':int
    }
}
user = get_user_info()
phone= get_phone_number(1)

DATA['url'] = "https://login.yahoo.com/account/create"
DATA['field']["first_name"] = "demitry"
DATA['field']["last_name"] = "vegas"
DATA['field']["email"] = "demitry.vegas@yahoo.com"
DATA['field']["password"] = "Azerty$$$123@"
DATA['field']["year_of_birth"] = 2000
DATA['field']['phone_number'] = phone[2:]

HOST = "38.143.183.202"
PORT = "92"


def my_proxy(PROXY_HOST,PROXY_PORT):
        fp = webdriver.FirefoxProfile()
        # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
        print (PROXY_PORT)
        print (PROXY_HOST)
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.http",PROXY_HOST)
        fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
        fp.set_preference("network.proxy.ssl",PROXY_HOST)
        fp.set_preference("network.proxy.ssl_port",int(PROXY_PORT))
        fp.set_preference("general.useragent.override","whater_useragent")
        fp.update_preferences()
        return webdriver.Firefox(firefox_profile=fp)

#browser = my_proxy(HOST,PORT)

browser = webdriver.Firefox()
browser.get(DATA['url'])
assert "Yahoo" in browser.title

def clear_and_input(ID,VALUE):
    elem = browser.find_element(By.ID,ID)
    elem.clear()
    elem.send_keys(VALUE)
    sleep(2)

def submit_data():
    browser.find_element(By.ID,"reg-submit-button").click()

clear_and_input("usernamereg-firstName",DATA['field']['first_name'])
clear_and_input("usernamereg-lastName",DATA['field']['last_name'])
clear_and_input("usernamereg-userId",DATA['field']['email'])
clear_and_input("usernamereg-password",DATA['field']['password'])
clear_and_input("usernamereg-birthYear",DATA['field']['year_of_birth'])
submit_data()
sleep(10)

clear_and_input("usernamereg-phone",DATA['field']['phone_number'])
submit_data()