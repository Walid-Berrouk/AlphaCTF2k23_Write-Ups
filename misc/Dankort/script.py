#! /usr/bin/python3

# Python3 program to validate Visa
# Card number using regular expression
import re

from luhn import *

import requests



divident  = 57568390651

# The next int will give us 17 digits
max_mult = 173708

cpt = 0
for i in range(max_mult + 1) :

    # must be a multpe of the divident
    tmp = str(divident*i)

    # Simple validation (verify is a funtion fromluhn package that verifies if a card number is valid)
    if tmp[:4] == "4571" and (len(tmp) == 13 or len(tmp) == 16) and verify(tmp) :

        print(f"Issuer: {data['bank']['name']}")
        print(tmp)

        # This code helps test iins using an api, helped in the beginning but gave a lot of possibilities
        # iin = tmp[:6]
        # try :
        #     response = requests.get(f"https://lookup.binlist.net/{iin}")
        #     if response.status_code == 200:
        #         data = response.json()
        #         print(f"Issuer: {data['bank']['name']}")
        #         print(tmp)
        #         cpt += 1
        #     else:
        #         print(f"Error: {response.status_code}")
        #         cpt = cpt
        # except :
        #     continue

print(f"cpt : {cpt}")