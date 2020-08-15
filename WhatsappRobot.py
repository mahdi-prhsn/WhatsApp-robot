from selenium import webdriver
from time import sleep
from selenium.webdriver.common import keys

#Here we set the path of the driver
driver = webdriver.Chrome(r'D:\chromedriver_win32\chromedriver.exe')

#Give the website address to driver
driver.get('https://web.whatsapp.com')

#application Usage
name = input('enter name:')
msg = input('enter ur message:')
count = int(input('how many times?'))
input('Press Enter')

#find the contact 
user = driver.find_element_by_xpath('//span[@title="%s"]'%name)
user.click()

#send the message 
msg_box = driver.find_element_by_class_name('_3u328')
for i in range(count):
    msg_box.send_keys(msg)
    btn = driver.find_element_by_class_name('_3M-N-')
    btn.click()