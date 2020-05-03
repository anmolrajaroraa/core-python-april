Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> bin(a)
'0b1010'
>>> b = bin(a)
>>> type(b)
<class 'str'>
>>> oct(a)
'0o12'
>>> # decimal number system -> 0-9
>>> # binary number system -> 0 and 1
>>> # octal number system -> 0-7
>>> # hexadecimal -> 0 - 15
>>> 11224334515
11224334515
>>> # hexadecimal -> 0 - 9, 10 -> A, 11 -> B, 12 -> C, 13 -> D, 14 -> E, 15 -> F
>>> #B2243345F
>>> bin(9999)
'0b10011100001111'
>>> oct(9999)
'0o23417'
>>> hex(9999)
'0x270f'
>>> b = '11110011110000'
>>> int(b)
11110011110000
>>> b = '0b11110011110000'
>>> int(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '0b11110011110000'
>>> b = 0b11110011110000
>>> int(b)
15600
>>> o = 0o23714
>>> int(o)
10188
>>> h = f027
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    h = f027
NameError: name 'f027' is not defined
>>> h = 0xf027
>>> int(h)
61479
>>> 