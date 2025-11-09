import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Email configuration
sender_email = "errorunknown3333@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "app_password"
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Create a message object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "open this niggesh"

# Email body
body = " WOMP WOMP "
message.attach(MIMEText(body, "plain"))

'''# Attach a file (optional)
file_path = "/home/devv/Downloads/DontOpen.txt"
attachment = open(file_path, "rb").read()
attach = MIMEApplication(attachment, _subtype="pdf")
attach.add_header("Content-Disposition", f"attachment; filename=YOU_ARE_COOKED.txt")
message.attach(attach)
'''

# Connecting to the SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Disconnect from the server
    server.quit()
