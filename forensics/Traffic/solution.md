# Traffic

## Description

> We captured this weird comunications. Can you investigate what is happening here......
> 
> Attachment : [chall.pcapng](chall.pcapng)

## Tags

> Network
> 
> Ping 

## Write-Up

```
tshark -r chall.pcapng -Y icmp.type==8 -T fields -e data >> out0.txt
```















Test here

<img src="./1.png"
     alt="Markdown Monster icon"
     style="
     width: 80%;
     diplay: box;"
/>


## Flag



## More Information

 - https://www.petermstewart.net/security-blue-team-vip-ctf-1-sneaky-transmission-write-up/
 - https://ctftime.org/writeup/23815
