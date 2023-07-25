from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chrome_driver_path = "D:\Development\chromedriver.exe"
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3526054785&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
EMAIL = "shotokillua55@gmail.com"
PASSWORD = "shotokillua55**"
PHONE_NUMBER = "7133519231"
ADDRESS = "281 Crownpointe Drive"
CITY = "Vallejo, California, United States"
ZIP = "94591"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Get to webpage and wait for page to load
driver.get(URL)
time.sleep(2)

# Click sign in button and wait for page to load
button = driver.find_element(By.CLASS_NAME, "btn-secondary-emphasis")
button.click()
time.sleep(2)

# Click username box and enter username
username = driver.find_element(By.ID, "username")
username.click()
username.send_keys(EMAIL)

# Click password box and enter password and press ENTER
pw = driver.find_element(By.ID, "password")
pw.click()
pw.send_keys(PASSWORD)
pw.send_keys(Keys.ENTER)
time.sleep(2)

# Go fullscreen, click easy apply button and wait
driver.fullscreen_window()
time.sleep(2)
easy_apply_button = driver.find_element(By.ID, "ember341")
easy_apply_button.click()
time.sleep(2)

# Click mobile phone number box and enter phone number and wait
phone_number_box = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3526054785-8370389589887919969-phoneNumber-nationalNumber"]')
phone_number_box.click()
phone_number_box.send_keys(PHONE_NUMBER)
time.sleep(1)

# Click next button and wait
next_button = driver.find_element(By.ID, "ember377")
next_button.click()
time.sleep(2)

street_addy = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3526054785-4890600030366046745-text"]')
street_addy.click()
street_addy.send_keys(ADDRESS)

city = driver.find_element(By.XPATH, '//*[@id="single-typeahead-entity-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3526054785-7539747367636040021-city-HOME-CITY"]')
city.click()
city.send_keys(CITY)
city.send_keys(Keys.ENTER)

# zip = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3526054785-5372406299473857582-text"]')
# zip.click()
# zip.send_keys(ZIP)

second_next = driver.find_element(By.ID, "ember508")
second_next.click()
time.sleep(2)

# third_next = find.driver(By.ID, "ember")