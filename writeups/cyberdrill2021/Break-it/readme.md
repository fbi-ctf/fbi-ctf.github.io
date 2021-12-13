## Break it!
Written By: **[0xAr7hur](https://twitter.com/0xAr7hur)** Date: `12-12-2021` Time: `13:45`

#### Description:
Link for [Artifact](https://drive.egovcloud.gov.bd/index.php/s/TtnH6IHHo6RLlSl/download) / 
[Artifact Mirror](https://github.com/fbi-ctf/fbi-ctf.github.io/blob/main/writeups/cyberdrill2021/Break-it/breakme.out)
Server to Connect [103.48.19.177:55555](http://103.48.19.177:55555/)

Your task is to extract the FLAG <br>
`The format for this flag is RE{flag}`

#### **Solution**

##### Basic File Check
Lets see some basic file checks we will use `file` and `checksec`  command to do that
```
┌──(r0otc0de㉿fs0ciety)-[~/ctf/cyberdrill]
└─$ file breakme.out && checksec breakme.out 
breakme.out: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=d4fb66a70c0961ea9e491c3361483a9beb92cee6, for GNU/Linux 3.2.0, not stripped
[*] '/home/r0otc0de/ctf/cyberdrill/breakme.out'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

##### Dynamic Analysis
For dynamic analysis open the file in `radare2 / IDA Pro / Ghidra / cutter`.
I'll use radare2 for now. You can also use any decompiler to do this.
Open Using:  `r2 ./breakme.out`

##### Radare2 Simple Basics
```nasm
┌──(r0otc0de㉿fs0ciety)-[~/Downloads/cyberdrill]
└─$ r2 ./breakme.out # opening the binary with radare2
[0x00001120]> aaa // `aaa` for analysis the binary
[0x00001120]> afl // `afl` to print all available functions
0x00001120    1 46           entry0
0x00001150    4 41   -> 34   sym.deregister_tm_clones
0x00001180    4 57   -> 51   sym.register_tm_clones
0x000011c0    5 57   -> 54   sym.__do_global_dtors_aux
0x000010a0    1 11           sym..plt.got
0x00001200    1 9            entry.init0
0x00001000    3 27           sym._init
0x00001520    1 5            sym.__libc_csu_fini
0x00001528    1 13           sym._fini
0x000012af    8 167          sym.SieveOfEratosthenes
0x000014b0    4 101          sym.__libc_csu_init
0x000013e6    7 196          sym.checkAndGetFlag
0x00001209    3 166          main
0x000010e0    1 11           sym.imp.printf
0x00001100    1 11           sym.imp.fflush
0x00001110    1 11           sym.imp.__isoc99_scanf
0x000010c0    1 11           sym.imp.__stack_chk_fail
0x00001356    5 51           sym.getFlag
0x00001389    9 93           sym.getpin
0x000010b0    1 11           sym.imp.puts
0x000010d0    1 11           sym.imp.system
0x000010f0    1 11           sym.imp.memset
[0x00001120]> s @ main // `s @ main` to select main function
0x1209
```
##### Radare2 Analysis
Use `pdf` command in radare2 to disassemble the current function in our case which is `main` 
The result:
```nasm
; DATA XREF from entry0 @ 0x1141
; var char *var_dh @ rbp-0xd
; var int64_t canary @ rbp-0x8
0x00001209      f30f1efa       endbr64
0x0000120d      55             push rbp
0x0000120e      4889e5         mov rbp, rsp
0x00001211      4883ec10       sub rsp, 0x10
0x00001215      64488b042528.  mov rax, qword fs:[0x28]
0x0000121e      488945f8       mov qword [canary], rax
0x00001222      31c0           xor eax, eax
0x00001224      488d3dd90d00.  lea rdi, str.Enter_the_pass_code:_ ; 0x2004 ; "Enter the pass code: " ; const char *format
0x0000122b      b800000000     mov eax, 0
0x00001230      e8abfeffff     call sym.imp.printf         ; int printf(const char *format)
0x00001235      488b05e42d00.  mov rax, qword [obj.stdout] ; obj.stdout__GLIBC_2.2.5
                                                           ; [0x4020:8]=0
0x0000123c      4889c7         mov rdi, rax                ; FILE *stream
0x0000123f      e8bcfeffff     call sym.imp.fflush         ; int fflush(FILE *stream)
0x00001244      488d45f3       lea rax, [var_dh]
0x00001248      4889c6         mov rsi, rax
0x0000124b      488d3dc80d00.  lea rdi, str.__4s           ; 0x201a ; " %4s" ; const char *format
0x00001252      b800000000     mov eax, 0
0x00001257      e8b4feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
0x0000125c      488d45f3       lea rax, [var_dh]
0x00001260      4889c6         mov rsi, rax
0x00001263      488d3db50d00.  lea rdi, str.__s_n          ; 0x201f ; " %s\n" ; const char *format
0x0000126a      b800000000     mov eax, 0
0x0000126f      e86cfeffff     call sym.imp.printf         ; int printf(const char *format)
0x00001274      b800000000     mov eax, 0
0x00001279      e831000000     call sym.SieveOfEratosthenes
0x0000127e      488d45f3       lea rax, [var_dh]
0x00001282      ba00000000     mov edx, 0                  ; int64_t arg3
0x00001287      be04000000     mov esi, 4                  ; int64_t arg2
0x0000128c      4889c7         mov rdi, rax                ; int64_t arg1
0x0000128f      e852010000     call sym.checkAndGetFlag
0x00001294      b800000000     mov eax, 0
0x00001299      488b4df8       mov rcx, qword [canary]
0x0000129d      6448330c2528.  xor rcx, qword fs:[0x28]
0x000012a6      7405           je 0x12ad
0x000012a8      e813feffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
; CODE XREF from main @ 0x12a6
0x000012ad      c9             leave
0x000012ae      c3             ret
```

After analysis we can see that its taking 4 integer as our input as we can see below at `0x0000124b` `0x00001257` this two addresses:
```nasm
0x0000124b      488d3dc80d00.  lea rdi, str.__4s           ; 0x201a ; " %4s" ; const char *format
0x00001252      b800000000     mov eax, 0
0x00001257      e8b4feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
0x0000125c      488d45f3       lea rax, [var_dh]
```
So the possible passcode would be in the range from 0000 to 9999

##### Getting the flag
After analysing the binary I came to a result to make a bash script to get all the possible combination for 0000-9999 and run it with the binary

solver.sh :
```bash
#!/usr/bin/env bash
for i in {0000..9999}; do echo $i | ./breakme.out ; done
```

running the script:
```
┌──(r0otc0de㉿fs0ciety)-[~/Downloads/cyberdrill]
└─$ chmod +x solver.sh && ./solver.sh  
Enter the pass code:  0000
Try again!
```

after some time we got something like that:
```
Enter the pass code:  2357
cat: /root/breakme/flag.txt: Permission denied
Try again!
```

As we can see that when the passcode is `2357` the binary was looking for the flag file(`/root/breakme/flag.txt`) 
So the passcode is (`2357`), I tried the pass code in the server
```bash
┌──(r0otc0de㉿fs0ciety)-[~/Downloads/cyberdrill]
└─$ nc 103.48.19.177 55555
Enter the pass code: 2357
{Aft3r 30 y3ar5 3veryon3's a good man. It'5 th3 law}
 2357
```
And we got the flag

**Flag**: `RE{Aft3r 30 y3ar5 3veryon3's a good man. It'5 th3 law}`
