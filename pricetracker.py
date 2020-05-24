# A simple web scraper and tracker made for testing purposes by Rohit R Nair.
# Make sure to go to google less secure apps and enable it before running this script for mail access.
import requests
from bs4 import BeautifulSoup
import smtplib
import time

USER="yourmailhere@gmail.com"                       # sender's mail/your mail
RECP_USER="recieversmailhere@srmist.edu.in"         # recipient mail/your mail
PWD="passwordhere"                                  # password of your mail

# URL of your target site where item is
URL='https://www.amazon.in/1971-P47-Bluetooth-Headphones-Microphone/dp/B07KNNVY1B/ref=sr_1_1?dchild=1&keywords=headphones&qid=1590351176&s=boost&sr=1-1&srs=10894223031&th=1'

# best to replace with your user agent
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}  

# function to check for price
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    # id of the item in your specified link
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    if(converted_price<500.00):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    # default smtp port and configs for gmail
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(USER, PWD)

    # Custom gmail message to execute
    subject = 'The Headphones Price fell down!'
    body = 'Check this out! : https://www.amazon.in/1971-P47-Bluetooth-Headphones-Microphone/dp/B07KNNVY1B/ref=sr_1_1?dchild=1&keywords=headphones&qid=1590351176&s=boost&sr=1-1&srs=10894223031&th=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        USER,
        RECP_USER,  
        msg
    )
    print('EMAIL SENT SUCCESSFULLY!')
    # quits the service once condition met.
    server.quit() 
    # disable this if you want to keep it running it forever.
    

# Condition to keep the loop running forever
while(True):
    check_price()
    time.sleep(60 *60)
    # 60sec * 60 min = 1hr