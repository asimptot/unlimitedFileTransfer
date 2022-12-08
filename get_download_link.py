from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import warnings
import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

warnings.filterwarnings("ignore")
options = Options()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("https://toffeeshare.com/")
sleep(5)

print('Enter your file directory: \n'
      'For Example: C:\\asd\\def\\filename.extension')
path = input()

for file in glob.glob(path):
    driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(file)

sleep(5)
print(driver.find_element(By.XPATH, "//*[@id='share-url']").get_attribute("value"))
element_present = EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Long term')]"))
WebDriverWait(driver, 1000).until(element_present)
