"""
This script checks wether the number of downloaded files matches the number of requested files downloaded from: from http://zinc.docking.org/
It also prompts to the terminal the names and locations of curropted files.
"""

from os import listdir, getcwd
from os.path import join, isdir
import gzip


ultimate_cuont = 0
empty_folders = 0
empty_categories = []

def proper_file(item):
	return item.find('17') < 0 #and item[0] in 'EF'


cwd = getcwd()
downloads = []

for item in listdir(cwd):
	if isdir(item) and proper_file(item):
		downloads.append(item)

for directory in downloads:
	files = listdir(join(cwd,directory))
	for file in files:
		to_expand = listdir(join(cwd,directory,file))
		if not to_expand:
			empty_folders += 1
			empty_categories.append(directory+file)
		else:
			for item in to_expand:
				try:
					with gzip.open(join(cwd,directory,file,item), 'r') as content:
						string_content = str(content.read())
						ultimate_cuont += string_content.count('@<TRIPOS>MOLECULE')
				except Exception as e:
					print(e, 'in:',join(cwd,directory,file,item))
					print('Count so far is', ultimate_cuont)

print('The total number of molecules:', ultimate_cuont)
print('Empty folders:', empty_folders)
with open('Empty Categories.txt', 'w') as output_file:
	for category in empty_categories:
		output_file.write(category + '\n') 
