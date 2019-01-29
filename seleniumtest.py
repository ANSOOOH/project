from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800,600))
display.start()
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("http://www.naver.com")
print(driver.page_source)
