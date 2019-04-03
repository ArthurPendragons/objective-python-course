import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
username = 'themainhero@gmail.com'
password = 'Password'
conn.starttls()

conn.login(username.password)
conn.sendmail(username,username)