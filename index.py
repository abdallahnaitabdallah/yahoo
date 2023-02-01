from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import csv

NUMBER_TO_CREATE = 1
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
1960,1959,1958]

PHONE_NUMBERS = ['447539798824', '447495861062', '447956026762', '447497628805', '447377340929', '447535235556', '447432462459', '447984821669', '447946267155', '447984023412', '447949356192', 
'447399815288', '447956654135', '447951681731', '447949681382', '447984025306', '447376672378', '447494146425', '447376640548', '447377738929', '447946629923', '447539082508', '447495355913', 
'447508855279', '447944896805', '447497629290', '447534794503', '447538455760', '447497628641', '447399392462', '447539570675', '447932315066', '447940434579', '447908596784', '447377342355', 
'447940057278', '447943620978', '447947571192', '447944636913', '447494200429', '447495595456', '447939118856', '447497425011', '447852314518', '447487257661', '447539962385', '447506789908', 
'447497629244', '447852648602', '447399393684','447377891429', '447508813401', '447931045017', '447495393365', '447375344329', '447535118189', '447947115316', '447398798953', '447951658577', 
'447539118025', '447984458966', '447947149127', '447535235652', '447496519783', '447377689594', '447497902140', '447377378589', '447946297451', '447939490101', '447984488947', '447377330522', 
'447496034833', '447951681849', '447949350051', '447946297156', '447399070042', '447497602240', '447958127749', '447949940079', '447904312035', '447908575423', '447506772909', '447939123442', 
'447508856074', '447984030944', '447496034941', '447497628787', '447932841183', '447432801961', '447497629326', '447939122213', '447377830102', '447984023414', '447930721915', '447947115160', 
'447946297714', '447984138582', '447983130939', '447904204539', '447507811348', '447943633916', '447399393808', '447949617452', '447903697484', '447398794475', '447539979514', '447497629220', 
'447497344899', '447983132095', '447939128173', '447495854722']

HOST = ["46.37.124.22","46.37.124.23","89.163.252.127","89.163.252.114","185.38.149.144","185.38.149.146","185.38.149.147","185.38.149.29","185.38.149.78","185.38.149.74","185.38.149.76",
"46.37.124.24","185.38.149.171","46.37.124.20","89.163.252.111","89.163.252.108","185.158.241.20","185.158.241.21","185.158.241.18","185.158.241.17","185.158.241.19",
"185.38.149.145","185.38.149.75",
"185.38.149.29","46.37.124.24","185.44.76.85","185.38.149.147","46.37.124.22","185.44.77.22","51.89.75.41","185.38.149.75","185.44.76.81",
"185.44.77.23","51.89.75.39","185.44.77.26","51.89.75.37","51.89.75.38","185.38.149.171","46.37.124.23","185.44.77.25","185.44.76.84","185.44.76.82","185.44.76.83","185.38.149.146",
"185.38.149.145","185.38.149.78","46.37.124.20","51.89.75.40","185.44.77.27","46.37.124.21","185.38.149.144","185.38.149.74","185.38.149.76","89.163.252.111","89.163.252.114","89.163.252.127",
"89.163.252.108","185.158.241.20","185.158.241.21","185.158.241.18","185.158.241.17","185.158.241.19","212.129.47.153","212.129.47.117","212.129.47.128",]
PORT = "92"

username = 'abdallah_nait'
pwd = 'Nait_abdallah592@'

url = "https://login.yahoo.com/account/create"
phones = list()
def get_user_info(browser:webdriver):
    
    browser.find_element(By.ID,'genbtn').click()
    user = browser.find_element(By.CLASS_NAME,'address').find_element(By.TAG_NAME,'h3').text
    user = user.split(' ')
    del user[1]
    firstname= str(user[0])
    lastname = str(user[1])
    browser.close()
    return firstname, lastname
def get_user_num(browser:webdriver):
    browser.switch_to.window(browser.window_handles[0])
    element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "select"))
    )
    while True:
        try:
            num = random.choice(PHONE_NUMBERS)
            element = Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(num)
            return num
        except:
            print("num doesnt exist ")
    
def get_validation_code(browser):
    print("start check validation ")
    sleep(8)
    browser.switch_to.window(browser.window_handles[0])
    sleep(10)
    browser.find_element(By.TAG_NAME,"form").submit()
    tables = browser.find_elements(By.TAG_NAME,"table")
    code = tables.find_elements(By.TAG_NAME,"tr")[3].text
    print (code)
    
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
    with open('mails.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def create():
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
    firstname,lastname = get_user_info(browser)
    num = get_user_num(browser)
    # fill all user data in DATA dict

    DATA["first_name"] = firstname
    DATA["last_name"] = lastname
    DATA["email"] = firstname+"_"+lastname+"_"+str(random.randint(1,1000))
    DATA["password"] = "Azerty$$$123@"
    DATA["year_of_birth"] = random.choice(YEARS)
    DATA['phone_number'] = num[2:]

    #save the user information in USER_INFO list
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])

    browser.get(url)
    assert "Yahoo" in browser.title
    clear_and_input("usernamereg-firstName",DATA['first_name'],browser)
    clear_and_input("usernamereg-lastName",DATA['last_name'],browser)
    clear_and_input("usernamereg-userId",DATA['email'],browser)
    clear_and_input("usernamereg-password",DATA['password'],browser)
    clear_and_input("usernamereg-birthYear",DATA['year_of_birth'],browser)
    submit_data(browser)
    sleep(1)
    valid = False
    while valid !=True:
        try:
            clear_and_input("usernamereg-phone",DATA['phone_number'],browser)
            submit_data(browser)
            error_element = browser.find_element(By.ID,"reg-error-phone").text
            if(error_element != None ):
                num = get_user_num(browser)
                DATA['phone_number'] = num[2:]
                browser.switch_to.window(browser.window_handles[1])
            else:
                valid = True
        except:
            valid=True
            save_csv(DATA.values())   

    get_validation_code(browser)    


for i in range(NUMBER_TO_CREATE):
    create()

