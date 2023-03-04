#! /usr/bin/python3


from pwn import *

HOST = 'challenges.ctf.alphabit.club'
PORT = 1001

p = remote(HOST, PORT)

print(p.recvline())
print(p.recvline())
p.sendline(b'1')

# The sum of coef
print(p.recvline())


