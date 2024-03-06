from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 


def get_dell_model(serial):
    url = f'https://www.dell.com/support/home/en-us/product-support/servicetag/{serial}/overview'

    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument("log-level=3")
    driver = webdriver.Edge(options=options)
    driver.get(url)
    element = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "hddSystemDescription")))
    model = element.get_attribute("innerText")
    driver.quit()
    return model
