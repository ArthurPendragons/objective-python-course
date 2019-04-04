##########################
# IMPORTS
import smtplib,openpyxl
#
##########################

#FUNCTIONS

def getName(number):
	return sheet.cell(row=number, column=1).value.split()[0]

def getEmail(number):
	return sheet.cell(row=number, column=2).value

def getAsset(number):
	return sheet.cell(row=number, column=3).value

def getCurrentVersion(number):
	return sheet.cell(row=number, column=4).value

def getType(number):
	return sheet.cell(row=number, column=5).value

def getMake(number):
	return sheet.cell(row=number, column=6).value

def getModel(number):
	return sheet.cell(row=number, column=7).value

######################################################################

workbook = openpyxl.load_workbook('email_list.xlsx')
sheet = workbook['Sheet1']
email = 'J.burgess@lancaster.ac.uk'
username = 'burgess@lancaster.ac.uk'
password = ''
conn = smtplib.SMTP('smtp.office365.com',587)
conn.starttls()
conn.login('burgess@lancaster.ac.uk','')
#print(username,password)




for x in range(2,5):
	currentName = getName(x)
	currentEmail = getEmail(x)
	currentAsset = getAsset(x)
	currentCurrentVersion = getCurrentVersion(x)
	currentType = getType(x)
	currentMake = getMake(x)
	currentModel = getModel(x)
	messageSubject = 'Subject: Windows 10 Upgrade\n\n'
	message = '''
Hi {name},\n
We are doing a scan of our systems and can see that you have an outdated version
of windows. Our scan shows that you are on {currentversion}.\n
The machine in question is your {make}{model} with the asset tag: {asset}.\n
\n
We please ask that you upgrade your machine via the windows update services as soon as possible.
If the option is not available, we please ask you to manually update using the windows assistant tool.\n
This can be found here: https://lancaster.box.com/s/x1piw2mda9hduq126uwq26zuux2eb71q\n\n

If you need any assistance with this, please do get in touch.\n\n

Thanks!\n
Jake
	'''.format(name=currentName,currentversion=currentCurrentVersion,make=currentMake,model=currentModel,asset=currentAsset)

	conn.sendmail(email,currentEmail,messageSubject+message)
	print('Email sent to: {}'.format(currentEmail))






