import random

flag = "fake_flag_for_testing"
def num_to_word(word):
    new_word = word
    numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    for j in word:
        if ord(j) in range(48, 58):
            new_word = new_word.replace(j, '-' + numbers[int(j)] + '-')
    return new_word

def pass_stars(word):
    num_stars = 15
    word_list = list(word)
    subword = {}
    for i in range(0, num_stars):
        b = False
        while not b:
            x = random.randint(0, len(word_list)-1)
            if (word_list[x] != '*') and (word_list[x] != '-'):
                subword[x] = word_list.pop(x)
                word_list.insert(x, '*')
                b = True
            else:
                b = False
    sub = []
    for k, v in sorted(subword.items()):
        sub.append(v)
    return [''.join(word_list), ''.join(sub)]

def randomize(word):
    chars = '&~#[]|`\^@$£%!?;:,.§<>=+/)(éèçà'
    lword = list(word)
    num_char = 50
    for k in range(0,num_char):
        lword.insert(random.randint(0,len(word)-1), chars[random.randint(0,len(chars)-1)])
    return ''.join(lword)

def to_bin(word):
    binary = []
    res = []
    for w in word:
        binary.append(bin(ord(w))[2:].zfill(8))
    for i in binary:
        for j in i:                
            res.append('one' if j == '1' else 'zero')
    return (' '.join(res))










result = pass_stars(flag)
random_result = randomize(result[0])
f = open('flag.txt', 'w')
f.write(result[1] + '\n')
res = to_bin(random_result)
f.write(res)
f.close()
