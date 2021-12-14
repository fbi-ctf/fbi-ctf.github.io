# Reverse-Engineering-up-to-date
Written By: **[0xAr7hur](https://twitter.com/0xAr7hur)** Date: `14-12-2021` Time: `14:35`

Artifects Will Be Available in our [github](https://github.com/fbi-ctf/fbi-ctf.github.io/tree/main/writeups/cyberdrill2021/Reverse-Engineering-up-to-date)

#### Short Solution

- binary check
  - `strings breakmesir` you can see `pydata` at bottom
- extracting pyc files from binary
  - Use [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor/blob/master/pyinstxtractor.py) to extracting pyc files from binary
- decompiling pyc back into equivalent Python source code
  - use [uncompyle6](https://pypi.org/project/uncompyle6/) to get the original Python source code
- review the source code
- writing script to automate the decryption process
  - Use [Python Script](https://github.com/fbi-ctf/fbi-ctf.github.io/blob/main/writeups/cyberdrill2021/Reverse-Engineering-up-to-date/breakmesir_solution.py) to get the Flag

### Detailed Video WriteUp
A Detailed Video solution By our team member **[OtolKhan](https://twitter.com/KhanOtol)** 
### Youtube [Video Link](https://www.youtube.com/watch?v=gBSYH4u-VHc)

##### Follow Us On twitter [@fbictf](https://twitter.com/fbictf)
##### Join Our [Discord Server](https://discord.gg/qhRJsKhBcX)
