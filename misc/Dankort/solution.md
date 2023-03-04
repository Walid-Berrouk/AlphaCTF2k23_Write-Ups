# Dankort

## Description

> The flag for this challenge is a valid visa card number that can be devided by 57568390651. (ps: the number is unique) format: AlphaCTF{credit_card_number}

## Tags

> Programming

## Write-Up

Let's search for some properties on VISA Cards :

 - The credit card number is a 13 or 16-digit number grouped in slots of 4.
 - The first digit is always a 4, which indicates that the card is a Visa card. 
 - The next 6 digits make up the issuer identifier number, which identifies the bank or financial institution that issued the card.
 - The remaining digits make up the account number, and the final digit is a check digit used to ensure that the card number is valid.


From that, we construct a script that tests numbers depending on conditions of the challenge :

 - From title of the challenge, we conclude that the finacial institue is `Dankort`

> The IIN (Issuer Identification Number) for Dankort is 4571. This is the first six digits of the 16-digit Dankort card number, and it identifies the card as a Dankort card. The remaining digits in the card number identify the specific cardholder and account. When a Dankort card is used for a transaction, the IIN is used to identify the issuing bank or financial institution, which enables the transaction to be processed and authorized.

 - The number is dividable by `57568390651`

The script :

```python
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
```

From that we get :

```
4571793743549165
```

## Flag

AlphaCTF{4571793743549165}
