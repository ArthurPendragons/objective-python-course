# Step 1 - Import required packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# Step 2 - Create message object instance
msg = MIMEMultipart()
 
# Step 3 - Create message body
message = "Test from Python via AuthSMTP"
 
# Step 4 - Declare SMTP credentials
password = "FalconPunch9000"
username = "J.burgess@lancaster.ac.uk"
smtphost = "securesmtp.lancs.ac.uk:587"

# Step 5 - Declare message elements
msg['From'] = "J.burgess@lancaster.ac.uk"
msg['To'] = "J.burgess@lancaster.ac.uk"
msg['Subject'] = "Test from Python via AuthSMTP"
 
# Step 6 - Add the message body to the object instance
msg.attach(MIMEText(message, 'plain'))
 
# Step 7 - Create the server connection
server = smtplib.SMTP(smtphost)
 
# Step 8 - Switch the connection over to TLS encryption
server.starttls()
 
# Step 9 - Authenticate with the server
server.login(username, password)
 
# Step 10 - Send the message
server.sendmail(msg['From'], msg['To'], msg.as_string())

# Step 11 - Disconnect
server.quit()
 
# Step 12 - 
