import os
import shelve
import shutil # shell utilities



# print(os.path.abspath('spam.png'))

# print(os.path.exists('spam.png'))
# baconFile = open('.\\bacon.txt','a')
# baconFile.write('Bacon is king!\n'*10)


# shelfFile = shelve.open('mydata')

# shelfFile['cats'] = ['Blacky','Ted','Belle']
# shelfFile.close()

# shelfFile = shelve.open('mydata')
# print(shelfFile['cats'])


# newShelf = shelve.open('repos')
# newShelf['reposits'] = ['git-projects','python-learning','javascript-playing']


# print(list(newShelf.keys()))


for foldername,subfolders,filename in os.walk('c:\\users\\Boo'):
	if subfolders == 'website':
		print(foldername)
