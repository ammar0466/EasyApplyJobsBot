from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print(driver.capabilities['browserVersion'])
print(driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0])
driver.quit()