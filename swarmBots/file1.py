from PIL import Image

img  = Image.open('M.jpg')
img = img.resize((64,64),Image.ANTIALIAS)
pix = img.load()
size = img.size
print size
for i in range(size[0]):
	for j in range(size[1]):
		if sum(pix[j,i])>100:
			pix[j,i] = (255,255,255)
			print "-",
		else:
			pix[j,i] = (0,0,0)
			print "0",
	print ""
img.save("outpic.jpg")