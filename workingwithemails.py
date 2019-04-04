import smtplib, openpyxl

conn = smtplib.SMTP('smtp.gmail.com', 587)
username = 'themainhero@gmail.com'
password = ''
receive_email = 'jake.p.burgess@gmail.com'
message = 'Subject: Testing Email Service\n\nHi, Jake\nThis is an automated generated email'

conn.starttls()

conn.login(username,password)
conn.sendmail(username,receive_email,message)