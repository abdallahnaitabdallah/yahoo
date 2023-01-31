from selenium import webdriver
from selenium.webdriver.common.by import By
#set proxy import 
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from getUserdata import get_user_info,get_validation_code
# manage time sleep 
from time import sleep
import random
#csv 
import csv

USER_INFO = []
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
YEARS = [2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,
1990,1989,1988,1987,1986,1985,1984,1983,1982,1981,
1980,1979,1978,1977,1976,1975,1974,1973,1972,1971,
1970,1969,1968,1967,1966,1965,1964,1963,1962,1961,
1960,1959,1958,1957,1956,1955,1954,1953,1952,1951,
1950,1949,1948,1947,1946,1945,1944,1943,1942,1941,
1940,1939,1938,1937,1936,1935,1934,1933,1932,1931,
1930,1929,1928,1927,1926,1925,1924,1923,1922,1921,
1920,1919,1918,1917,1916,1915,1914,1913,1912,1911,
1910,1909,1908,1907,1906,1905,1904,1903,1902,1901]

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


def clear_and_input(ID,VALUE):
    elem = browser.find_element(By.ID,ID)
    elem.clear()
    elem.send_keys(VALUE)
    sleep(2)

def submit_data():
    browser.find_element(By.ID,"reg-submit-button").click()


def create():
    browser = my_proxy(HOST,PORT)
    #browser = webdriver.Firefox()
    
    browser.get('https://www.fakenamegenerator.com/gen-random-us-uk.php')
    
    # create new tab for vsimcard and log in 
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
   
    browser.get("https://vsimcard.com/login.php")
    assert "Vsimcard" in browser.title
    browser.find_element(By.NAME,"username").send_keys(username)
    sleep(1)
    browser.find_element(By.NAME,"password").send_keys(pwd)
    sleep(1)
    browser.find_element(By.TAG_NAME,"form").submit()
    sleep(5)
    
    user = get_user_info(browser)
    code_validation = get_validation_code(browser):
             
    # fill all user data in DATA dict
    DATA['url'] = "https://login.yahoo.com/account/create"
    DATA['field']["first_name"] = user["firstname"]
    DATA['field']["last_name"] = user["lastname"]
    DATA['field']["email"] = user["firstname"]+"_"+user["lastname"]+"_"+random.randint(1,1000)
    DATA['field']["password"] = "Azerty$$$123@"
    DATA['field']["year_of_birth"] = random.choice(YEARS)
    DATA['field']['phone_number'] = user["phone"]
    
    #save the user information in USER_INFO list
    USER_INFO.append(DATA["field"])
    
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[2])
    browser.get(DATA['url'])
    assert "Yahoo" in browser.title

    clear_and_input("usernamereg-firstName",DATA['field']['first_name'])
    clear_and_input("usernamereg-lastName",DATA['field']['last_name'])
    clear_and_input("usernamereg-userId",DATA['field']['email'])
    clear_and_input("usernamereg-password",DATA['field']['password'])
    clear_and_input("usernamereg-birthYear",DATA['field']['year_of_birth'])
    submit_data()
    sleep(10)

    clear_and_input("usernamereg-phone",DATA['field']['phone_number'])
    submit_data()
   
def save_csv(data):
    myFile = open('yahoo_users.csv', 'w')
    writer = csv.writer(myFile)
    writer.writerow(['first_name', 'last_name', 'email','password','year_of_birth','phone_number'])
    for user in data:
        writer.writerow(user.values())
    myFile.close()

    
    

    
