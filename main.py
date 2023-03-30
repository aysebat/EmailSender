import os
import yagmail
import time
from datetime import datetime as dt
import pandas as pd

sender = '2023.python.project@gmail.com'
receiver= 'llkhsokg@drope.ml'

subject="The autometed email sender python project"

contents="""
Hello!
This email was sent for the automated email sender Python project.
"""

def send_email_every_minute():
  while True:
   
    yag = yagmail.SMTP(user=sender,
                        password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print('Email Send!')
    time.sleep(60)
    
def send_email_with_arrrenged_time():
  while True:
    now = dt.now()
    print(now)
    if now.hour==3 and now.minute==23:
      yag = yagmail.SMTP(user=sender,
                        password=os.getenv('PASSWORD'))
      yag.send(to=receiver, subject=subject, contents=contents)
      print('Email Send!')
      time.sleep(60)

#send_email_with_arrrenged_time()

def send_email_to_csv_contacts():
  """This function send to email to the people listed in csv file
The csv file containss the name and email combination, separated by commas. 
  """
  #read the csv file using pandas 
  df = pd.read_csv("contacts.csv")

  #iterate over all rows
  for index, row in df.iterrows():
    
    subject="The autometed email sender python project"

    #customize the contant with name from the csv file
    contents=f"""
    Hello {row['name']}
    This email was sent to the automated email sender 
    Python project.
  
    Best Wishes.
    """
  
    yag = yagmail.SMTP(user=sender,
                      password=os.getenv('PASSWORD'))
    #send the email list to the csv file 
    yag.send(to=row['email'], 
             subject=subject, 
             contents=contents)
    print('Email Send!')


#send_email_to_csv_contacts()  
