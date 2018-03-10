import zipfile
import os

def get_next_file(text):
	start = text.find("Next nothing is ")
	return text[start + len("Next nothing is "):]

def loop_through_files(zip_archive, starting_file):
	i = 0
	file = starting_file
	comments = ''

	with zipfile.ZipFile(zip_archive, 'r') as myzip:
		while i < 1000:
			with myzip.open(file) as myfile:
				info = myzip.getinfo(file)
				comments += info.comment
				data = myfile.read()
				if "Next nothing is " in data:
					file = get_next_file(data) + ".txt"
				else:
					print file, data
					break
				i += 1
	return comments

print(loop_through_files('channel.zip', '90052.txt'))