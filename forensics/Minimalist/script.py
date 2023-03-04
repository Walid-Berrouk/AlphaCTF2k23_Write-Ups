with open("chall.bin", mode="rb") as file:
    contents = file.read()

# Forge png back, couldn't complete it

header = b""

## Magic Byte 
magic = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"
header += magic

# IHDR

chunk_tupe_ihdr = b"\x00\x00\x00\x0d\x49\x48\x44\x52"
header += chunk_tupe_ihdr
# width 154 - 0x9a
sizes = b"\x00\x00\x00\x9a\x00\x00\x00\x02"
header += sizes

bit_length = b"\x08"
color_type = b"\x02"
other = b"\x00\x00\x00"
crc = b"\x12\x16\xf1\x4d"

header += bit_length + color_type + other + crc

with open('chall.png', 'wb') as f:
    f.write(header + contents)

print("PNG Created !")