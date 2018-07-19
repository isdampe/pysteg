from PIL import Image
import numpy as np
import sys, bits

src_img = Image.open(sys.argv[1])
pixels = np.array(src_img)

out_buffer = []

x = 0
y = 0
for i in range(int(sys.argv[2])):
	buffer = 0
	for j in range(8):
		pixel = pixels[x][y]	
		bit = bits.get_bit(pixel[0], bits.LSB)
		buffer = bits.set_bit(buffer, j, bit)
		x += 1
		if x >= src_img.width:
			x = 0
			y += 1
	out_buffer.append(buffer)

fh = open(sys.argv[3], "wb")
fh.write(bytes(out_buffer))