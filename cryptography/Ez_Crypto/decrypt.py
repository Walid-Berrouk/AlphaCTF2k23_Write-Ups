# From bin to chars

def to_chars(bins) :
    lbins = bins.split()

    new_bins = []
    cpt = 0
    some_bin = ""
    for i in lbins :
        
        cpt += 1
        # Test
        if i == "zero" :
            some_bin += "0"
        else :
            some_bin += "1"
        
        if cpt % 8 == 0 :
            new_bins.append(some_bin)
            some_bin = ""
            cpt = 0
    
    new_chars = []
    for b in new_bins :
        new_chars.append(chr(int(b, 2)))
    
    return new_chars

def flag_back(enc, chars) :
    chars_forbidden = '&~#[]|`\^@$£%!?;:,.§<>=+/)(éèçà'

    flag_stars = ""
    for i in chars :
        if i in chars_forbidden :
            continue

        flag_stars += i

    # Get flag back

    cpt = 0
    flag = ""
    for i in flag_stars :
        if i == "*" :
            flag += enc[cpt]
            cpt += 1
        else :
            flag += i
    
    return flag


f = open("flag.txt")

result = f.readlines()
chars = to_chars(result[1])

print(flag_back(result[0], chars))