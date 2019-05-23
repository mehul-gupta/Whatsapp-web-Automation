#import necessary modules
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import random

#load chrome_driver
driver = webdriver.Chrome(r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe')

driver.get("https://web.whatsapp.com/")

#Wait for the user to scan the QR-code
wait = WebDriverWait(driver, 600)

good_morning_messages=["Good Morning! :)","Wake up..its late :D","Have a nice day!!","Heyy there.."]

done=0
wish_morning=0

#Schedule time to send the message
scheduled_time=str(input('Enter time at which you want to send the message(HH:MM): '))
h=int(scheduled_time.split(":")[0])
m=int(scheduled_time.split(":")[1])    

#Specify group/contacts to whom we want to send the message
target = str(input('Enter name of person/group you want to send message to:'))

#Keep the bot running
while True:
    
    #Identify time
    cur_time=datetime.datetime.now() 
    time=cur_time.time()
    cur_hour=time.hour
    cur_min=time.minute
    
    #Wish "Good Morning" at specified time
    if wish_morning==0 and cur_hour==h and cur_min==m:
        
        #Select random greeting
        string = good_morning_messages[random.randrange(0,100)%4]

        #Identify correct text input panel (search bar)
        x_arg = '//span[contains(@title, '+ '"' +target + '"'+ ')]'
        group_title = wait.until(EC.presence_of_element_located((
                By.XPATH, x_arg)))
        group_title.click()

        #Identify correct text input panel (chat box)
        inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"]'
        input_box = wait.until(EC.presence_of_element_located((
                By.XPATH, inp_xpath)))

        #Send message, and set flag to indicate done for day
        input_box.send_keys("Hi " + target + ", " + string + Keys.ENTER)
        wish_morning=1
        print("Message sent at",str(h)+":"+str(m))

    #Reset flag
    if cur_hour!=h or cur_min!=m:
        wishmorning=0