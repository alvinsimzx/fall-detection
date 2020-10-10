#email module
# module for sending emails
import smtplib # library to send emails

# variables to store sender user details
PERCENTAGE = 0.7

# accepts 5 confidence levels in float, receiver email, subject and body
# returns true if success & sends mail to receiver
#c1, c2, c3, c4, c5, 
def send_email(aReceiverEmail, aSubject, aBody):
    # context manager, makes sure connection is closed automatically
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        '''
        avg = (c1 + c2 + c3 + c4 + c5) / 5

        if (avg < PERCENTAGE):
            print("Confidence level too low!")
            return False
        '''
        smtp.ehlo() # identifies self with the mail server that we are using
        smtp.starttls() # encrptys the traffic
        smtp.ehlo()

        smtp.login("raspberrydummy@gmail.com", "raspberry12345")

        lMsg = f'Subject: {aSubject}\n\n{aBody}'

        # email_sender, email_receiver, message
        smtp.sendmail("raspberrydummy@gmail.com", aReceiverEmail, lMsg)

        print("Alert Email Sent!")
        return True
        
