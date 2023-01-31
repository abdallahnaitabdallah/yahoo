from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
from time import sleep
import random
import csv
NUMBER_TO_CREATE = 2
USER_INFO = []
DATA = {
    "proxy":str,
    'first_name':str,
    'last_name':str,
    'email':str,
    'password':str,
    'year_of_birth':int,
    'phone_number':int
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

HOST = ["46.37.124.22","46.37.124.23","89.163.252.127","89.163.252.114","185.38.149.144","185.38.149.146","185.38.149.147","185.38.149.29","185.38.149.78","185.38.149.74","185.38.149.76",
"46.37.124.24","185.38.149.171","46.37.124.20","89.163.252.111","89.163.252.108","185.158.241.20","185.158.241.21","185.158.241.18","185.158.241.17","185.158.241.19",
"185.38.149.145","185.38.149.75"]
PORT = "92"

username = 'abdallah_nait'
pwd = 'Nait_abdallah592@'

url = "https://login.yahoo.com/account/create"

def get_user_info(browser:webdriver,index:int):
     
    browser.find_element(By.ID,'genbtn').click()
    user = browser.find_element(By.CLASS_NAME,'address').find_element(By.TAG_NAME,'h3').text
    user = user.split(' ')
    del user[1]
    firstname= str(user[0])
    lastname = str(user[1])
    browser.switch_to.window(browser.window_handles[0])
    select = Select(browser.find_element(By.TAG_NAME, "select")).select_by_index(index)
    return firstname,lastname

def get_validation_code(browser) -> int:

    browser.switch_to.window(browser.window_handles[1])
    browser.find_element(By.TAG_NAME,"form").submit()
    return 0
    
def my_proxy(PROXY_HOST,PROXY_PORT):
    
    fp = webdriver.FirefoxProfile()
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http",PROXY_HOST)
    fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
    fp.set_preference("network.proxy.ssl",PROXY_HOST)
    fp.set_preference("network.proxy.ssl_port",int(PROXY_PORT))
    fp.set_preference("general.useragent.override","whater_useragent")
    fp.update_preferences()
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    browser = webdriver.Firefox(executable_path=r'C:\\WebDrivers\\geckodriver.exe', firefox_binary=binary,firefox_profile=fp)
    return browser

def clear_and_input(ID,VALUE,browser):
    elem = browser.find_element(By.ID,ID)
    elem.clear()
    elem.send_keys(VALUE)
    sleep(1)

def submit_data(browser):
    browser.find_element(By.ID,"reg-submit-button").click()

def save_csv(data):
    myFile = open('hotmail.csv', 'w')
    writer = csv.writer(myFile)
    writer.writerow(['proxy','first_name', 'last_name', 'email','password','year_of_birth','phone_number'])
    for user in data:
        writer.writerow(user.values())
    myFile.close()

def create(index):
    DATA["proxy"] = random.choice(HOST)
    browser = my_proxy(DATA["proxy"],PORT)

    browser.get("https://vsimcard.com/login.php")
    browser.find_element(By.NAME,"username").send_keys(username)
    sleep(1)
    browser.find_element(By.NAME,"password").send_keys(pwd)
    sleep(1)
    browser.find_element(By.TAG_NAME,"form").submit()
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("https://www.fakenamegenerator.com/gen-random-us-uk.php")
    firstname,lastname = get_user_info(browser,index)
    # fill all user data in DATA dict

    DATA["first_name"] = firstname
    DATA["last_name"] = lastname
    DATA["email"] = firstname+"_"+lastname+"_"+str(random.randint(1,1000))
    DATA["password"] = "Azerty$$$123@"
    DATA["year_of_birth"] = random.choice(YEARS)
    DATA['phone_number'] = 713123123123

    #save the user information in USER_INFO list
    USER_INFO.append(DATA)
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[2])

    browser.get(url)
    assert "Yahoo" in browser.title
    clear_and_input("usernamereg-firstName",DATA['field']['first_name'],browser)
    clear_and_input("usernamereg-lastName",DATA['field']['last_name'],browser)
    clear_and_input("usernamereg-userId",DATA['field']['email'],browser)
    clear_and_input("usernamereg-password",DATA['field']['password'],browser)
    clear_and_input("usernamereg-birthYear",DATA['field']['year_of_birth'],browser)
    submit_data(browser)
    sleep(2)
    clear_and_input("usernamereg-phone",DATA['field']['phone_number'],browser)
    submit_data(browser)

    if index ==NUMBER_TO_CREATE:
        save_csv(USER_INFO)
        browser.close()


for i in range(NUMBER_TO_CREATE):
    create(i+1)

