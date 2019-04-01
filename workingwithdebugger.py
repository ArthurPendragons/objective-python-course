import os

readEmails = open('emails.txt','r')

for emails in readEmails():
	print(emails)

