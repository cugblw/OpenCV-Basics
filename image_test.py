from PIL import Image

img = Image.open('13_6184_3573.png')
rgba = img.convert("RGBA")
datas = rgba.getdata()

newData = []
for item in datas:
	if item[0] < 2 and item[1] < 2 and item[2] < 2: # finding black colour by its RGB value
		# storing a transparent value when we find a black colour
		newData.append((0, 0, 0, 0))
	else:
		newData.append(item) # other colours remain unchanged

rgba.putdata(newData)
rgba.save("transparent_image.png", "PNG")
