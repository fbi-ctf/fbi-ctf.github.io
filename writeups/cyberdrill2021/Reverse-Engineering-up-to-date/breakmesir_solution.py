# Taken From OtolKhan's official GitHub Repo: `https://github.com/otolk/python/blob/main/breakmesir_solution.py`

import base64, binascii
x= "675a0425011a63520e5859361901362e091132120c3c243f0e0222050f3b655727770968"
flag = list(binascii.unhexlify(x))
print(flag)
res = "U"
answer="U"
for i in range(len(flag)-1):
    res = chr(flag[i]^ord(res))
    answer+=res
print(answer)
print(base64.b64decode(answer))
