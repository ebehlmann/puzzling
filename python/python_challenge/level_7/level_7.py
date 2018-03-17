from PIL import Image

def get_gray_color_list(img_data, start_pixel, end_pixel):
	grays = []
	i = start_pixel
	while i < end_pixel:
		grays.append(img_data[i][0])
		i += 7
	return grays

def ascii_to_letter(characters):
	result = ''
	for char in characters:
		result += chr(char)
	return result

#load image
img = Image.open('oxygen.png')
data = img.getdata()

#get center band to work with
width = img.width
height = img.height
start_of_center_row = width * (height/2)
end_of_center_row = start_of_center_row + width

#get pixel list for center row
grays = get_gray_color_list(data, start_of_center_row, end_of_center_row)

#convert ascii values to letters
message1 = ascii_to_letter(grays)
print(message1)

#get section of message 1 that is between brackets
message2_start = message1.index('[')
message2_end = message1.index(']')
asciis = message1[message1.index('[') + 1:message1.index(']')]

# split into a list and convert to integers 
asciis_list = asciis.split(', ')
asciis_int = []
for i in asciis_list:
	asciis_int.append(int(i))

#get final message
print(ascii_to_letter(asciis_int))