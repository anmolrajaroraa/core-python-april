Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1 + 2
3
>>> 1 - 2
-1
>>> 1 * 2
2
>>> 1 / 2
0.5
>>> 1 % 2
1
>>> 35353/43
822.1627906976744
>>> round( 35353/43 )
822
>>> round( 822.567 )
823
>>> 35353 / 43  # classic division (long-division method)
822.1627906976744
>>> #single-line comment
>>> 35353 // 43
822
>>> #  // -> floor division
>>> 
>>> pow(2,10)
1024
>>> 2 ** 10 # same as pow()
1024
>>> # int, float, string, boolean, byte, complex
>>> a = 10
>>> a = 10.2  # dynamic typing
>>> type(a)
<class 'float'>
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = "hello world"
>>> type(a)
<class 'str'>
>>> a = true
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a = true
NameError: name 'true' is not defined
>>> a = True
>>> type(a)
<class 'bool'>
>>> a = False
>>> ord #ordinal fn - unicode / ascii value is returned
<built-in function ord>
>>> ord
<built-in function ord>
>>> ord("a")
97
>>> ord(" ")
32
>>> chr(50)
'2'
>>> chr(100)
'd'
>>> chr(125)
'}'
>>> chr(225)
'á'
>>> chr(250)
'ú'
>>> 
>>> chr(8304)
'⁰'
>>> name = "Ram"
>>> name
'Ram'
>>> name = "Ramराम "
>>> name
'Ramराम '
>>> name.encode()
b'Ram\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae '
>>> x = name.encode()
>>> type(x)
<class 'bytes'>
>>> x
b'Ram\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae '
>>> x.decode()
'Ramराम '
>>> 
