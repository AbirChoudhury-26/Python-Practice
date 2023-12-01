from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def sleeping():
  time.sleep(3)

chrome_driver_path = '/usr/local/bin/chromedriver'


chrome_options = webdriver.ChromeOptions()                             # Helps in creating an instance of the Chrome Options class, help in cong var. settings and prefrences for Chrome Browser
service = Service(chrome_driver_path)                                  # Helps on Specifying path of our chrome driver and healso helps in confg webdriver service. Im short ,it tells Selenium WebDriver to find Chrome Binary file
driver = webdriver.Chrome(service=service, options=chrome_options)     # Creates an instance of the Chrome WebDriver.

# Open a website
# driver.get('https://www.saucedemo.com/')

    # Page Navigating and Clicking elements
time.sleep(5)

# try:
#   username= driver.find_element(By.ID,"user-name")
#   password= driver.find_element(By.ID,"password")
#   loginButton= driver.find_element(By.ID,"login-button")

#   username.send_keys("standard_user")
#   password.send_keys("secret_sauce")

#   loginButton.send_keys(Keys.ENTER)
#   time.sleep(5)
#   print("Login Successful")

  
#   # try:
#   #   element = WebDriverWait(driver, 10).until(
#   #       EC.presence_of_all_elements_located((By.LINK_TEXT,"Sauce Labs Backpack")))
#   #   element.click()

#   # except:
#   #   print("Link didn't clicked ")
#   #   #driver.quit()
#   try:
#     link=driver.find_element(By.LINK_TEXT,"Sauce Labs Backpack")
#     link.click()
#   except:
#     print("Link not clicked")

#   print("Successfully Executed Each Stage!!!")
# except:
#   print("Unsuccessful")
#   #driver.quit()


# username= driver.find_element(By.ID,"user-name")
# password= driver.find_element(By.ID,"password")
# loginButton= driver.find_element(By.ID,"login-button")

# username.send_keys("standard_user")
# password.send_keys("secret_sauce")

# loginButton.send_keys(Keys.ENTER)
# sleeping()
# print("Login Successful")

# try:
#   link=driver.find_element(By.LINK_TEXT,"Sauce Labs Backpack")
#  # link=driver.find_element(By.CLASS_NAME,"inventory_item_name ")
#   link.click()
#   sleeping()

#   print("Link Clicked successfully")
#   sleeping()
# except:
#   print("Link not clicked")


# addToCart=driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack")
# addToCart.click()
# sleeping()

# #remove= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,"remove-sauce-labs-backpack")))

# try:

#   # remove= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(By.XPATH,"//button[@name='remove-sauce-labs-backpack']"),"Remove")

#   element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element(
#       (By.XPATH, "//button[@name='remove-sauce-labs-backpack']"),  "Remove"
#       )
# )
#   print(element)
#   removeButton= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME,"remove-sauce-labs-backpack")))
#   removeButton.click()
#   print("Remove button clicked")

# except Exception as e:
#   print("Exception problem : ",  e)



# Performing some methods like : Submit button, Alert & pop up handling

# driver.get("https://qavalidation.com/demo-form/")
# time.sleep(5)
# form=driver.find_element(By.XPATH,"//form[@class='contact-form commentsblock wp-block-jetpack-contact-form']")

# time.sleep(25)

# try:

#   form.submit()
#   print("Success!!")
# except:
#   print("Fail")

driver.get("https://nxtgenaiacademy.com/alertandpopup/")

# popup=driver.find_element(By.NAME,"promptalertbox1234")
# popup.click()
# time.sleep(2)

# alert = driver.switch_to.alert

# time.sleep(5)

# # Get the text from the alert
# alert_text = alert.text
# print(f"Alert Text: {alert_text}")

# # Accept the alert (you can use dismiss() to cancel the alert)
#alert.accept()

