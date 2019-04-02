import smtplib

conn = smtplib.SMTP('smtp.office365.com', 587)

print(conn.ehlo())