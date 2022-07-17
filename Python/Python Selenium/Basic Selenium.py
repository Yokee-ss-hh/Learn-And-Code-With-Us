import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Type pip show selenium in Terminal for selenium version

browser = webdriver.Chrome(service = Service("C:\\PythonSelenium\\chromedriver_win32 (1)\chromedriver.exe"))

url = 'https://youtube.com'

browser.get(url)

print(browser.title)

search_bar = browser.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys('techwithtim')

search_click_btn = browser.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon").click()

print(browser.title)

print(selenium.__version__)








