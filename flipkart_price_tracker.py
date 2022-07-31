#author riyaz
from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
import time

link_url=input("Please Enter The Url :")
desired_price=int(input("Enter The Desired Price :"))
print("Thank You I Will Be Notifying You Once The Price Drops")
webdriver_path =r"C:\Users\riyaz\Desktop\python_scripts\chromedriver.exe"
service_obj = Service(webdriver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
def price_check():
    try:
        driver.get(link_url)
        time.sleep(3)
        name=driver.find_element(By.CLASS_NAME,"B_NuCI").text
        print(name)
        price=driver.find_element(By.CLASS_NAME,"_30jeq3._16Jk6d").text
        converted_price=float(price.replace("₹","").replace(",","").replace(" ",""))
        print(converted_price)
        if (converted_price<=desired_price):
            send_message("\n" "\n"+name+"\n" "\n"+str(price)+"\n" "\n"+link_url)
            # time.sleep(60)
        else:
            print("*Not At Your Desired Price")
        
    except:
        print("There Is Some Error Ill Try To Fix It ")

def send_message(bot_message):
    
    bot_token = 'Your Telegram Bot Token'
    bot_chatID = 'Your Telegram Chat Id'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
while(True):
    price_check()
    time.sleep(5)
