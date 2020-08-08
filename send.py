from twilio.rest import Client
from creditionals import *
import time
import random
client = Client(account_sid, auth_token)




c = 0
b = 3

while c != b:
    my_msg =   random.randint(1000, 9999)
    message = client.messages.create(to=my_cell, from_=my_twilio,body=my_msg)
    print("Msg has been sent")

    time.sleep(2)

    a = int(input("Enter the number: "))
    
    

    
    if a == my_msg:
        print("Correct OTP")
        time.sleep(2)
        break
    
    else:
        print("Try Again with new OTP")
        time.sleep(2)
        c += 1

          
          
