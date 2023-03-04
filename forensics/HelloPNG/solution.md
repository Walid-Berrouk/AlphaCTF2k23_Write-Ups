# HelloPNG

## Description

> I build this image from scratch and applied a FILTER I bet you know PNG better than me can you reveal the secret from this .....
> 
> Attachment: [Challenge.png](Challenge.png)

## Tags

> PNG 
>
> IDAT 

## Write-Up

From the description of the challenge, we can see that the author used a specia Filter in the png to generate the picture, so let's first extract that filter.

After decomposing the image, we can easily get the filter bits like following :

```py
...
i = 0
filter_array = []
for r in range(height): # for each scanline
    filter_type = IDAT_data[i] # first byte of scanline is filter type
    filter_array.append(filter_type)
    ...
```

wet get :

```
[1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0]

length : 180
```

After that, we might be tempted to generaate bytes from this set of bits, we try sets of 7 and 8 bites :

```py
....
# 8 bits
bytes2 = []

for i in range(0, len(filter_array), 8) :
    tmp = ""

    for i in filter_array[i: i + 8] :
        tmp += str(i)
    bytes2.append(tmp)

flag = ""
for i in bytes2 :
    flag += chr(int(i, 2))


print(flag)

# 7 bits
bytes1 = []

for i in range(0, len(filter_array), 7) :
    tmp = ""

    for i in filter_array[i: i + 7] :
        tmp += str(i)
    bytes1.append(tmp)

flag = ""
for i in bytes1 :
    flag += chr(int(i, 2))


print(flag)
```

From there we get :

```
³0êF÷Îy5¿Kùºîú
AlphaCTF{f1Lter5_b1T_fun}
```

## Flag

AlphaCTF{f1Lter5_b1T_fun}

## More Information

 - http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html
 - Writing a (simple) PNG decoder might be easier than you think : https://pyokagan.name/blog/2019-10-14-png/
