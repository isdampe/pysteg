LSB = 0x0
MSB = 0x7

def get_bit(byte, n):
	return (byte >> n) & 0x1

def set_bit(byte, n, value):
	mask = 1 << n
	byte &= ~mask
	if value:
		byte |= mask
	return byte
