import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


import zlib
import struct

with open("chall.bin", mode="rb") as file:
    contents = file.read()


splited_chunk = contents.split(b'IDAT')

# Length of data
chunk_length = int.from_bytes(splited_chunk[0], "big")

# chunck IDAT
IDAT_data = zlib.decompress(splited_chunk[1][:chunk_length])


# Set Size
width = 154
# rgb : 3 bytes per pixel
# height = idat_length / (1 + width * 3) 
height = round(len(IDAT_data) / (1 + width*3))

Recon = []
bytesPerPixel = 3
stride = width * bytesPerPixel

i = 0
for r in range(height): # for each scanline
    filter_type = IDAT_data[i] # first byte of scanline is filter type
    i += 1
    for c in range(stride): # for each byte in scanline
        # Since filter type is already given (0), so we affect directly (origin)
        Filt_x = IDAT_data[i]
        i += 1
        Recon_x = Filt_x
        Recon.append(Recon_x) # truncation to byte

# plt.imshow(np.array(Recon).reshape((height, width, 3)))
# plt.show()

# Convert the pixels into an array using numpy
array = np.array(Recon, dtype=np.uint8).reshape((height, width, 3))

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('flag.png')