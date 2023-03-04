requests= open("out1.txt","r").readlines()


need=[]

for  j in range(len(requests)) : 
    byte_str = bytes.fromhex(requests[j])
    need.append(chr(int(byte_str.decode())))


print(''.join(need))
# print(' '.join(''.join(need).replace('AlphaCTF{','').split('}')))



# Data :

# print(''.join(need))

# AlphaCTF{060ad92489947d410d897474079c1477}AlphaCTF{3e04873f1179f0d77767caf6f79416b3}AlphaCTF{79eb1bf6872845080574bee2ed56b86d}AlphaCTF{7c7409db65f8ff5bec078fd02d5de8d4}AlphaCTF{65a90070ad09e95403d454c0d17ee12b}AlphaCTF{1de4347eb5dcdb0f9addeb271725a506}AlphaCTF{ca1f4a7de4596979848397cc9d97de9c}AlphaCTF{358d7d89828ded802f1237178fd984bd}AlphaCTF{253f594e25dcd1057daf08cf267561a9}AlphaCTF{450e56122a0643f4350f31924e641207}AlphaCTF{19dcb24c39aa60dab989d192a0f55208}AlphaCTF{1c5a534ad7786ac4ebcc1d3e0c7276db}AlphaCTF{b277440f96b5b6da52e56c648be2d619}AlphaCTF{d4ede8817cc64ad4aef5ef7971119d1e}AlphaCTF{fc996de295b575f94a0838d1219c41ca}AlphaCTF{c860e3d5e7ccd57f7761e0a62d4ff67d}AlphaCTF{a6a1f37a326e98ecd22807c0b1b2f41c}AlphaCTF{e10ea7251ab94045244f8bb8fbcf697f}AlphaCTF{425361ad8c397f9bde3eef8f9277a417}AlphaCTF{966d71ab645a33f1fa0392dfeef76372}AlphaCTF{d8a5db3a5b6c70b1623bfd5e9ddfea9a}AlphaCTF{a84bda35469ef3e0a5eff09345cb5882}AlphaCTF{95cd636efcab44b2f56cf849ff12d3c6}AlphaCTF{5a72b5077e24763eba270cb99e4ca471}AlphaCTF{679b

# print(' '.join(''.join(need).replace('AlphaCTF{','').split('}')))

# 060ad92489947d410d897474079c1477 3e04873f1179f0d77767caf6f79416b3 79eb1bf6872845080574bee2ed56b86d 7c7409db65f8ff5bec078fd02d5de8d4 65a90070ad09e95403d454c0d17ee12b 1de4347eb5dcdb0f9addeb271725a506 ca1f4a7de4596979848397cc9d97de9c 358d7d89828ded802f1237178fd984bd 253f594e25dcd1057daf08cf267561a9 450e56122a0643f4350f31924e641207 19dcb24c39aa60dab989d192a0f55208 1c5a534ad7786ac4ebcc1d3e0c7276db b277440f96b5b6da52e56c648be2d619 d4ede8817cc64ad4aef5ef7971119d1e fc996de295b575f94a0838d1219c41ca c860e3d5e7ccd57f7761e0a62d4ff67d a6a1f37a326e98ecd22807c0b1b2f41c e10ea7251ab94045244f8bb8fbcf697f 425361ad8c397f9bde3eef8f9277a417 966d71ab645a33f1fa0392dfeef76372 d8a5db3a5b6c70b1623bfd5e9ddfea9a a84bda35469ef3e0a5eff09345cb5882 95cd636efcab44b2f56cf849ff12d3c6 5a72b5077e24763eba270cb99e4ca471 679b