# STEP-1 (import libs)
'''
1. package : twilio
2. module : rest
3. datetime, timedelta
4. time
5. getpass

'''
from twilio.rest import Client 
from datetime import datetime,timedelta
import time
import getpass

# STEP-2(twilio credentials)
'''
>> It is the first step for the authentication.
>> acc_sid and auth_token are specified here because we are using twlio's API (REST).
1. account_SID is the id which I created in twilio.
2. auth_token is the password of my account.

'''
account_SID = ''
auth_token = ''

#for using the API from twilio cloud.
''' 
Calling the API 
Creating twilio's Client class object 'client' for calling the API
This API helps to connect the WP server with twilio's server

'''
client = Client(account_SID, auth_token)
#client - object of the class Client.

'''Authentication DONE.
So basically it's a rule to call the API by authentication [acc_id, auth_token(password)]'''

#STEP-3 (Sending messages)
''''
Defining a function for sending messages

1. sender (from_)
2. message body (body)
3. reciever (recipient_no)

'''
def wp_msg(recipient_no, msg_body):

    try:

        msg = client.messages.create(
            from_= 'whatsapp:+14155238886',
            body=msg_body,
            to=f'whatsapp:{recipient_no}'
        )

        print(f'message sent successfully !')

    except Exception as e:

        print(f'Error occurred !')

# Step-4 (user input)
        
name = input(f'Enter recipient name : ')
reciever = getpass.getpass(f'Enter {name}''s number  "e.g (+91-**********)" : ')

while True: 

    message_body = input(f'Type message you want to send : ')

    # Step- 5 (Fixing time)

    date_str = input(f"Enter the date when you want to send message  (YYYY-MM-DD) : ")
    time_str = input(f"Enter the time when you want to send message  (HH : MM) : ")

    # step- 6 (calculating time)

    '''For converting the string formatted time from user to real date time by strptime(date_str, format)

    %H = 24 hours
    %M = minute
    %Y = year
    %m = month
    %d = date

    '''
    schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    current_time = datetime.now()

    # step - 7

    ''' Calculating the difference between current date and the message sending date'''
    difference = schedule_datetime-current_time
    delay_seconds = difference.total_seconds()
    '''This will convert your time dofference into seconds.'''

    # step - 8

    if delay_seconds<=0:

        print("Enter the correct date and time : ")

    else:

        time.sleep(delay_seconds)
        wp_msg(reciever, message_body)