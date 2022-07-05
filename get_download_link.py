from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings
import glob

warnings.filterwarnings("ignore")
options = Options()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("https://toffeeshare.com/")
time.sleep(5)

print('Enter your file directory: \n'
      'ig: C:\\asd\\def\\filename.extension')
path = input()

for file in glob.glob(path):
    driver.find_element_by_xpath('//input[@type="file"]').send_keys(file)

time.sleep(5)
print(driver.find_element_by_xpath("//*[@id='share-url']").get_attribute("value"))
time.sleep(120)