"""
 This script is written to be rn from H:\youssof\Gallery\Series\Mr. Robot\Season 2 1080p
 if you won't do so please adjust the in_file_nemes and out_file_names so you read from and write to
 the proper distinatino folder.
"""

from glob import glob

def add_n_to_time(hrs, mins, secs, n):
	return hrs + (mins + (secs+n) // 60) // 60, (mins + (secs+n) // 60) % 60, (secs+n) % 60
def to_time_str(hrs, mins, secs, msecs):
	return str(hrs) + ':' + str(mins) + ':' + str(secs) + ',' + msecs

in_file_names = glob('*.srt')
out_file_names = glob('*.mkv')

for in_file_name, out_file_name in zip(in_file_names, out_file_names):
	with open(in_file_name, 'r') as input_file:
		with open(out_file_name[:-4]+'.srt', 'w') as out_file:
			line = input_file.readline()
			while line:
				if line.find('-->') > 0:
					time_from = line.split(' --> ')[0].split(',')[0].split(':')
					time_to = line.split(' --> ')[1].split(',')[0].split(':')
					
					updated_time_from = add_n_to_time(int(time_from[0]), int(time_from[1]), int(time_from[2]), 5)
					updated_time_to = add_n_to_time(int(time_to[0]), int(time_to[1]), int(time_to[2]), 5)
					
					new_line =  to_time_str(updated_time_from[0], updated_time_from[1], updated_time_from[2], line.split(' --> ')[0].split(',')[1]) 
					new_line += ' --> '
					new_line += to_time_str(updated_time_to[0], updated_time_to[1], updated_time_to[2], line.split(' --> ')[1].split(',')[1]) 
					out_file.write(new_line)
				else:
					out_file.write(line)
				line = input_file.readline()