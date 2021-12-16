# Takduk Takdum
Written By: **[KaziBlackFox](https://twitter.com/KaziBlackFox)** Date: `16-12-2021`
<br>
Artifact will be available on our **[github](https://github.com/fbi-ctf/fbi-ctf.github.io/blob/main/writeups/cyberdrill2021/Takduk-Takdum/dislexia.pcapng)**

#### Description:
It is assumed that someone from inside the organization exchanged some recorded telephonic conversation. The network traffic captured and need to extract message from attached file.
<br>
`The format for this answer is Cyb3raud21{flag}`

#### Solution:
##### Basic file check
Lets see some basic file checks we will use file command

![basicFile](image/basicFile.jpg)

Here we see it's a packet capture file and we try some packet analysis in here but found nothing.
So i tried some basic command like foremost:

![foremost](image/foremost.jpg)

When open the file then i found some intresting things like wav file. then use file command to check that it's a wav file or not. 

![wav-check](image/wav-check.jpg)

when i insure that it's a wav file then i shifted it to audacity and change it to multi-view option.

![audacity](image/audacity.jpg)

and sound hear like some beep beep formation and i just convert the small to dot(.) and big to(-) and the encryption look like some morse code:

`. -..- ..-. .. .-.. - .-. .- - .. --- -.`


![cybercheif](image/cybercheif.jpg)

and when i decode it to cyber-chef  then  i found :
<br>
**Flag:** `Cyb3raud21{EXFILTRATION}`

##### Follow Us On twitter [@fbictf](https://twitter.com/fbictf)
##### Join Our [Discord Server](https://discord.gg/qhRJsKhBcX)
