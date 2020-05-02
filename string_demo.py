Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = "hello this is python programming and it is very easy"
>>> #indexing
>>> str2 = "hello"
>>> # char arr[] = ['h', 'e', 'l', 'l', 'o']
>>> # string is a collection of characters
>>> str2[0]
'h'
>>> str2[1]
'e'
>>> str2[2]
'l'
>>> str2[3]
'l'
>>> str2[4]
'o'
>>> len(str2)
5
>>> len(str1)
52
>>> str1[51]
'y'
>>> str1[10]
' '
>>> str1[20]
' '
>>> str1[2`]
SyntaxError: invalid syntax
>>> str1[21]
'p'
>>> # str1[ starting index : stopping index ]
>>> str1[ 0 : 15 ]
'hello this is p'
>>> str1[ 15 : 30 ]
'ython programmi'
>>> str1[ 30 : 50 ]
'ng and it is very ea'
>>> str1[ 50 : 100 ]
'sy'
>>> str1[100]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    str1[100]
IndexError: string index out of range
>>> str1[51]
'y'
>>> str1[ -1 : -4 ]
''
>>> # str1[ starting index : stopping index : step(increment in index) ]
>>> 
>>> str1[ 5 : 10 : 1]
' this'
>>> str1[ -1 : -4 ]
''
>>> str1[ -1 : -4 : -1]
'ysa'
>>> 
>>> str1[ 10 : -1 ]
' is python programming and it is very eas'
>>> str1[ 10 : 51 ]
' is python programming and it is very eas'
>>> str1[ 10 : 52 ]
' is python programming and it is very easy'
>>> str1[ 10 : 0 ]
''
>>> str1[ 10 : ]
' is python programming and it is very easy'
>>> 
>>> 
>>> str1 = "hello this is python programming and it is very easy to use because of simple syntax"
>>> str1[ 10 : -1 ]
' is python programming and it is very easy to use because of simple synta'
>>> str1[ 10 : -2 ]
' is python programming and it is very easy to use because of simple synt'
>>> str1[ 10 : 0 ]
''
>>> str1[ 10 ]
' '
>>> str1[ 10 : ]
' is python programming and it is very easy to use because of simple syntax'
>>> str1[ 0 : 50 ]
'hello this is python programming and it is very ea'
>>> str1[ : 50 ]
'hello this is python programming and it is very ea'
>>> str1
'hello this is python programming and it is very easy to use because of simple syntax'
>>> str1[ : ]
'hello this is python programming and it is very easy to use because of simple syntax'
>>> str1[ : : 2 ]
'hloti spto rgamn n ti eyes ouebcueo ipesna'
>>> str1[ : : 5 ]
'h  y rndirs bs ln'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> size
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    size
NameError: name 'size' is not defined
>>> sizeof
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    sizeof
NameError: name 'sizeof' is not defined
>>> str1.capitalize()
'Hello this is python programming and it is very easy to use because of simple syntax'
>>> str1.title()
'Hello This Is Python Programming And It Is Very Easy To Use Because Of Simple Syntax'
>>> str1 = "hello this is PYTHON programming and it is very easy to use because of simple syntax"
>>> str1.lower()
'hello this is python programming and it is very easy to use because of simple syntax'
>>> str1.upper()
'HELLO THIS IS PYTHON PROGRAMMING AND IT IS VERY EASY TO USE BECAUSE OF SIMPLE SYNTAX'
>>> 
>>> str1.swapcase()
'HELLO THIS IS python PROGRAMMING AND IT IS VERY EASY TO USE BECAUSE OF SIMPLE SYNTAX'
>>> heading = "Welcome to Stone Paper Scissors Zone"
>>> heading
'Welcome to Stone Paper Scissors Zone'
>>> heading.center(100)
'                                Welcome to Stone Paper Scissors Zone                                '
>>> heading.center(100, "*")
'********************************Welcome to Stone Paper Scissors Zone********************************'
>>> heading.center(90, "*")
'***************************Welcome to Stone Paper Scissors Zone***************************'
>>> str1.count('p')
2
>>> str1.count('P')
1
>>> str1.lower().count('p')
3
>>> str1.startswith("hello")
True
>>> str1.startswith("hellO")
False
>>> str1.endswith("hellO")
False
>>> str1.endswith("tax")
True
>>> str1.find('s')
9
>>> str1
'hello this is PYTHON programming and it is very easy to use because of simple syntax'
>>> str1.find('s', 10)
12
>>> str1.find('s', 13)
41
>>> str1.find('s', 42)
50
>>> str1.find('s', 51)
57
>>> str1.find('s', 58)
65
>>> str1.find('s', 66)
71
>>> str1.find('s', 72)
78
>>> str1[78:]
'syntax'
>>> str1.find('s', 79)
-1
>>> str1.index('s')
9
>>> str1.index('s',10)
12
>>> str1.index('s', 79)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    str1.index('s', 79)
ValueError: substring not found
>>>
Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> "ram123".isalnum()
True
>>> "ram_123".isalnum()
False
>>> "ram_123".isascii()
True
>>> "ram_123å".isascii()
False
>>> "ram_123å".isdecimal()
False
>>> "1234567890".isdecimal()
True
>>> $123 = "hello"
SyntaxError: invalid syntax
>>> var$123 = "hello"
SyntaxError: invalid syntax
>>> var_123 = "hello"
>>> print("Hello everyone this is python it's a beginner's language")
Hello everyone this is python it's a beginner's language
>>> print("Hello everyone \nthis is python \nit's a beginner's language")
Hello everyone 
this is python 
it's a beginner's language
>>> "a".isprintable()
True
>>> "\n".isprintable()
False
>>> str1 = "Hello everyone this is PYTHON it's a beginner's language"
>>> str1.isupper()
False
>>> str1.islower()
False
>>> str1.istitlw()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    str1.istitlw()
AttributeError: 'str' object has no attribute 'istitlw'
>>> str1.istitle()
False
>>> str1.split()
['Hello', 'everyone', 'this', 'is', 'PYTHON', "it's", 'a', "beginner's", 'language']
>>> str1.split("s")
['Hello everyone thi', ' i', " PYTHON it'", " a beginner'", ' language']
>>> str1.split("e")
['H', 'llo ', 'v', 'ryon', " this is PYTHON it's a b", 'ginn', "r's languag", '']
>>> str1
"Hello everyone this is PYTHON it's a beginner's language"
>>> str2 = ' it's very easy '
SyntaxError: invalid syntax
>>> str2 = " it's very easy "
>>> str2 = ' "python" is very easy'
>>> str2
' "python" is very easy'
>>>  ' "Women\'s day" '
 
SyntaxError: unexpected indent
>>> str3 = ' "Women\'s day" '
>>> str3
' "Women\'s day" '
>>> print(str3)
 "Women's day" 
>>> str3 = " \"Women's day\" "
>>> print(str3)
 "Women's day" 
>>> 
>>> str1.split()
['Hello', 'everyone', 'this', 'is', 'PYTHON', "it's", 'a', "beginner's", 'language']
>>> str1
"Hello everyone this is PYTHON it's a beginner's language"
>>> # str1 -> immutable
>>> str1
"Hello everyone this is PYTHON it's a beginner's language"
>>> str1[0]
'H'
>>> str1[0] = 'h'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    str1[0] = 'h'
TypeError: 'str' object does not support item assignment
>>> del str1[0]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    del str1[0]
TypeError: 'str' object doesn't support item deletion
>>> result = str1.split()
>>> type(result)
<class 'list'>
>>> str1
"Hello everyone this is PYTHON it's a beginner's language"
>>> result
['Hello', 'everyone', 'this', 'is', 'PYTHON', "it's", 'a', "beginner's", 'language']
>>> del result[2]
>>> result
['Hello', 'everyone', 'is', 'PYTHON', "it's", 'a', "beginner's", 'language']
>>> del result[2]
>>> result
['Hello', 'everyone', 'PYTHON', "it's", 'a', "beginner's", 'language']
>>> del result[3]
>>> result
['Hello', 'everyone', 'PYTHON', 'a', "beginner's", 'language']
>>> del result[3]
>>> result
['Hello', 'everyone', 'PYTHON', "beginner's", 'language']
>>> " ".join(result)
"Hello everyone PYTHON beginner's language"
>>> "***".join(result)
"Hello***everyone***PYTHON***beginner's***language"
>>> str4 = "http://cloudfront.net/index.mpd?token=abjdnksdmdlmdanl"
>>> str4.split()
['http://cloudfront.net/index.mpd?token=abjdnksdmdlmdanl']
>>> str4.split("=")
['http://cloudfront.net/index.mpd?token', 'abjdnksdmdlmdanl']
>>> str4 = "http://cloudfront.net/index.mpd?token=abjdnksdmdlmdanl$%^&*CHNCFGHJBBJN=^&*%^"
>>> str4.split("=")
['http://cloudfront.net/index.mpd?token', 'abjdnksdmdlmdanl$%^&*CHNCFGHJBBJN', '^&*%^']
>>> 
>>> str4.partition("=")
('http://cloudfront.net/index.mpd?token', '=', 'abjdnksdmdlmdanl$%^&*CHNCFGHJBBJN=^&*%^')
>>> 
>>> str4.split("=", 1)
['http://cloudfront.net/index.mpd?token', 'abjdnksdmdlmdanl$%^&*CHNCFGHJBBJN=^&*%^']
>>> str4.rsplit("=", 1)
['http://cloudfront.net/index.mpd?token=abjdnksdmdlmdanl$%^&*CHNCFGHJBBJN', '^&*%^']
>>> str4.rpartition("=")
('http://cloudfront.net/index.mpd?token=abjdnksdmdlmdanl$%^&*CHNCFGHJBBJN', '=', '^&*%^')
>>> 
>>> heading = "GAME ZONE"
>>> heading.center(90)
'                                        GAME ZONE                                         '
>>> heading.center(120)
'                                                       GAME ZONE                                                        '
>>> heading.ljust(120)
'GAME ZONE                                                                                                               '
>>> #ljust -> left justified, rjust -> right justified
>>> heading.rjust(120)
'                                                                                                               GAME ZONE'
>>> product = "             Analog Women's Watch - Fastrack                 "
>>> product.strip() #leading and trailing spaces will be removed
"Analog Women's Watch - Fastrack"
>>> str1
"Hello everyone this is PYTHON it's a beginner's language"
>>> str1.replace( 'H', 'h' )
"hello everyone this is PYThON it's a beginner's language"
>>> str1
"Hello everyone this is PYTHON it's a beginner's language"
>>> id(str1)
4432660832
>>> str1 = str1.replace( 'H', 'h' )
>>> id(str1)
4463282416
>>> str1
"hello everyone this is PYThON it's a beginner's language"
>>> str1.replace("PYThON", "C++")
"hello everyone this is C++ it's a beginner's language"
>>> str5 = "Hello everyone \nthis is python \nit's a beginner's language"
>>> str5.splitlines()
['Hello everyone ', 'this is python ', "it's a beginner's language"]
>>> str1.find("PYTHON")
-1
>>> str1.find("PYThON")
23
>>> str1[23]
'P'
>>> str1.find('PYThON')
23
>>> 
