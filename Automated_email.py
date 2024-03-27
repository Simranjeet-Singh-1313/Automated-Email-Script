import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time
import sys
TimeInterval=[58]

def Send_Email():
    Sender_email = "XYZ@gmail.com"  # change the email 
    Receiver_email = "ABC@gamil.com" # change the email 
    password = "uitm"  # change the password

    message = MIMEMultipart()
    message["From"] = Sender_email
    message["To"] = Receiver_email
    for j in TimeInterval:
        message["Subject"] = f"Career Opportunity Jobs{j}"

    Body = """


Hi all,
this is test email 
"""

    message.attach(MIMEText(Body, "plain"))

    # Attachments
    file_path = "file_sample.odt"  # After keeping the file in the same folder just use the ODT file name link I have added
    attachment = open(file_path, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename= file.odt")  # Replace file.odt with your desired filename

    message.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(Sender_email, password)
        server.sendmail(Sender_email, Receiver_email, message.as_string())
        #sys.exit() 
# Set the start time for the emails


# Schedule the sending of emails every second after the start time
for i in TimeInterval:
    schedule.every().day.at(f"00:29:{i}").do(Send_Email)
while True:
    schedule.run_pending()
    time.sleep(0.1)
