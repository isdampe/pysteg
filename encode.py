from PIL import Image
import numpy as np
import sys, bits

def array_image_save(array, image_path):
	image = Image.fromarray(array)
	image.save(image_path)

src_img = Image.open(sys.argv[1])
pixels = np.array(src_img)

fh = open(sys.argv[2], "rb")
binary_data = fh.read()

x = 0
y = 0
for i in range(len(binary_data)):
	buffer = binary_data[i]
	for j in range(8):
		pixel = pixels[x][y]	
		bit = bits.get_bit(buffer, j)
		pixel[0] = bits.set_bit(pixel[0], bits.LSB, bit)
		pixels[x][y] = pixel

		x += 1
		if x >= src_img.width:
			x = 0
			y += 1

array_image_save(pixels, sys.argv[3])
print("Encoded %s bytes" % len(binary_data))