
'''
*************
*           *
*           *
*           *
*************
'''
import traceback
import os

# def boxPrint(symbol,width,height):

# 	if len(symbol) != 1:
# 		raise Exception('Your *symbol* is not 1 characters long')
# 	if (width < 2) or (height < 2):
# 		raise Exception('Width needs to be higher than 2')
# 	print(symbol*width)
# 	for i in range(height-2):
# 		print(symbol + (' ' * (width-2)) + symbol)

# 	print(symbol*width)


# boxPrint('OO',10,3)



try:
	raise Exception('This is the error message')
except:
	errorFile = open('error_log.txt', 'a')
	errorFile.write(traceback.format_exc()+'\n')
	errorFile.close()
	print('Traceback information was stored in the log')