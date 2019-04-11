###########################
#INFO!
###########################
# THIS SCRIPT IS TO EMAIL A LIST OF USERS IN THE EXCEL SPREADSHEET, THE INFORMATION IS GENERATED BY ANOTHER SCRIPT
# OR DATA CAN BE EDITED MANUALLY.
# THIS IS IN PREPERATION FOR THE SOFTWARE REQUEST LIST THIS SUMMER.
###########################

##########################
# IMPORTS
import smtplib,openpyxl,datetime
#
##########################

#FUNCTIONS

def getName(number):
	return sheet.cell(row=number, column=1).value.split()[0]

def getEmail(number):
	return sheet.cell(row=number, column=2).value

def getCourse(number):
	return sheet.cell(row=number, column=3).value

def getSoftware(number):
	return sheet.cell(row=number, column=4).value

def getVM(number):
	return sheet.cell(row=number, column=5).value

def getDate(number):
	return sheet.cell(row=number, column=7).value

def getLab(number):
	return sheet.cell(row=number, column=6).value	

######################################################################

currentTime = datetime.date.today()
workbook = openpyxl.load_workbook('Software_requests.xlsx')
sheet = workbook['Sheet1']
email = 'J.burgess@lancaster.ac.uk'
username = 'burgess@lancaster.ac.uk'
conn = smtplib.SMTP('smtp.office365.com',587)
conn.starttls()
conn.login('burgess@lancaster.ac.uk','PASSWORD')

######################################################################

for x in range(2,5):
	currentName = getName(x)
	currentEmail = getEmail(x)
	currentCourse = getCourse(x)
	currentSoftware = getSoftware(x)
	currentVM = getVM(x)
	currentLab = getLab(x)
	currentDate = getDate(x)
	messageSubject = 'Subject: Lab Software Requests\n\n'

	message = '''
Hi {name},\n\n
We have yet to hear from you regarding the software requirements for {course}.\n
Currently you are scheduled to be a {lab} Lab, our labs contain a core set of software which can be found here: https://lancaster.box.com/s/0o4mwiu3x1wluy551p3ye23lvwdccmx8\n\n
Apart from the software in this set, last year when your course was taught this software set was required:\n\n
{software}\n\n
Last year, you {vm} use a VM. Will you be needing one?\n\n
If you need any changes to this can you please let me know asap. We are currently preparing the above list for the labs, upgrading  all applications to latest versions to minimize any security issues.\n\n
Please can you let me know as soon as possible, if your requirements don't arrive in time we will work from last years requirements. \n\n
Thanks!

Jake
'''.format(name=currentName,course=currentCourse,lab=currentLab,vm=currentVM,software=currentSoftware)

	conn.sendmail(email,currentEmail,messageSubject+message)
	print('Email sent to: {}'.format(currentEmail))

	if currentDate == None:
		sheet.cell(row=x,column=7).value = currentTime
	else:
		sheet.cell(row=x,column=8).value = currentTime


########################################################################

workbook.save('Software_requests.xlsx')
