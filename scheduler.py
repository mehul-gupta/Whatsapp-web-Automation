from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import random

driver = webdriver.Chrome(r'C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe')

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

good_morning_messages=["What's up? :D","Good Morning! :)","Rise and Shine. :3","I'm up!"]

done=0
wish_morning=0

#Keep the bot running
while True:
    
    #Identify time
    cur_time=datetime.datetime.now() 
    time=cur_time.time()
    cur_hour=time.hour
    cur_min=time.minute

    #Wish "Good Morning" at 06:00 am
    if wish_morning==0 and cur_hour==14 and cur_min==41:
        
        Target = ["akshat"]
        #Iterate over selected contacts
        for target in Target:

            #Select random greeting
            string = good_morning_messages[random.randrange(0,100)%4]

            #Identify correct text input panel (search bar)
            x_arg = '//span[contains(@title, '+ '"' +target + '"'+ ')]'
            group_title = wait.until(EC.presence_of_element_located((
                    By.XPATH, x_arg)))
            print(x_arg)
            group_title.click()

            #Identify correct text input panel (chat box)
            inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"]'
            input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath)))

            #Send message, and set flag to indicate done for day
            input_box.send_keys("Hi " + target + ", " + string + Keys.ENTER)
            wish_morning=1

    #Reset flag
    if cur_hour!=14 or cur_min!=41:
        wishmorning=0