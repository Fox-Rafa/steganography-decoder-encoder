from PIL import Image, ImageDraw
from binary_decoder import letterToDecimal
from binary_decoder import bynarriToDecimal


print('do you want to encode or decode?')
print('write "encode" if you want to encode or "decode" if you want to decode')
enDe = input()

if enDe == 'encode':

	#print('do you want to create a new image or write into an existing image?')
	#print('write "create" to create a new image or "write" to write into existing image')
	#ans = input()

	#if ans=='create' or ans=='Create':
	#	print('what will the image file be caled?')
	#	imageName = input()
	#	image = Image.new('RGB', (160,160), color='black')
	#	imageName = imageName + '.png'
	#	image.save(imageName)

	#else:
	#	print('what is the existing image name?')
	#	imageName = input()
	#	image = Image.open(imageName)

	print('what will the image file be caled?')
	imageName = input()
	image = Image.new('RGB', (160,160), color='black')
	imageName = imageName + '.png'
	image.save(imageName)

	print('what will you like to write')
	output = ''
	Input = input()
	Input = str(Input)
	for letr in Input:
		answer = letterToDecimal(letr)
		output = output+answer

	print(output)
	g = len(output)/3
	gg = g + 1
	gg = int(gg)
	#print (gg)
	#print(len(output))
	pixels = image.load()
	pixels[0, 0] = (gg, 2, 2)
	h = 0

	for p in range(gg):
	#    pixels[1,p+1] = (int(output[h]), int(output[h+1]), int(output[h+2]))
	#    print(int(output[h]), int(output[h+1]), int(output[h+2]))
		k = len(output) - h
	#    print('-', k)
		if k == 1 :
			pixels[int(p)+1, 0] = (int(output[h]), 2, 2)
		if k == 2 :
			pixels[int(p)+1, 0] = (int(output[h]), int(output[h+1]), 2)
		if k > 2 :
			pixels[int(p)+1, 0] = (int(output[h]), int(output[h+1]), int(output[h+2]))
		h = h + 3

	image.save(imageName)
	image.show()

#-----------------------------------------------------------------

if enDe == 'decode':
	print('what image will you like to decode?')
	deImage = input()
	img = Image.open(deImage)
	pixel = img.load()
	n, n2, n3 = pixel[0,0]
	bits = ''
	for l in range(n):
		r, g, b = pixel[int(l+1),0]
		bits = bits+str(r)
		bits = bits+str(g)
		bits = bits+str(b)

	bits = bits.replace('2','')
	print(bits)
	x = bits
	ln = len(x)
	ln = int(ln)
	u = ln/8
	u = int(u)
	awnser = 'nada'
	finalawnser = ''
	for i in range(u):
		al = (i+1)*8
		y = x[al-8]
		y = y+(x[al-7])
		y = y+(x[al-6])
		y = y+(x[al-5])
		y = y+(x[al-4])
		y = y+(x[al-3])
		y = y+(x[al-2])
		y = y+(x[al-1])
		
		output = bynarriToDecimal(y)

		finalawnser = finalawnser + output
	print(finalawnser)





