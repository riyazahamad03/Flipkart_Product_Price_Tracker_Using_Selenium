import selenium
from selenium import webdriver
import requests
import datetime
import time
import getpass
link_url=input("Please Enter The Url :")
desired_price=int(input("Enter The Desired Price :"))
print("Thank You I Will Be Notifying You Once The Price Drops")
webdriver_path =r"C:\Users\riyaz\Desktop\python_scripts\chromedriver.exe"
driver=webdriver.Chrome(webdriver_path )
def price_check():
    try:
        
        driver.get(link_url)
        time.sleep(3)
        name=driver.find_element_by_class_name("B_NuCI").text
        print(name)
        price=driver.find_element_by_class_name("_30jeq3._16Jk6d").text
        converted_price=float(price.replace("₹","").replace(",","").replace(" ",""))
        print(converted_price)
        if (converted_price<=desired_price):
            send_message("\n" "\n"+"Hey Riyaz Price Fell Down Grab It Fast "+"\n" "\n"+name+"\n" "\n"+str(price)+"\n" "\n"+link_url)
        else:
            print("*Not At Your Desired Price")
        
    except:
        print("There Is Some Error Ill Try To Fix It ")

def send_message(bot_message):
    
    bot_token = '1145135629:AAEOUYNdMrO7eujmgjlHdhvjK1E-2XYnIYY'
    bot_chatID = '620621191'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
while(True):
    price_check()
    time.sleep(4)