from selenium import webdriver

from selenium.webdriver.common.by import By 

from time import sleep

from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

# task01 - back()
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(5)
print(driver.title)
driver.get("https://www.google.com/")
print(driver.title)
driver.back()
print(driver.title)

#task02
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(5)
print(driver.title)
driver.get("https://www.google.com/")
sleep(5)
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)


#task03
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(5)
print(f'Current URL: {driver.current_url}')
driver.refresh
print(f'Current URL: {driver.current_url}')

#task04
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(5)
driver.close()

#task05
driver.get("https://opensource-demo.orangehrmlive.com/")
sleep(5)
driver.quit()

