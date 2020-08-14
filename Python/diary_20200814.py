Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: /home/user/EDIBO/Python/OOP_test_1.py ===============
Before an = PartyAnimal()
After an = PartyAnimal()
Before first an = an.party()
So far x is 1
After firest an = an.party()
Before second an = an.party()
So far x is 2
After second an = an.party()
Before third an = an.party()
So far x is 3
After third an = an.party()
Before one more party()
So far x is 4
After one more party()
>>> 
=============== RESTART: /home/user/EDIBO/Python/OOP_test_1.py ===============

Before an = PartyAnimal()
After an = PartyAnimal()

Before first an = an.party()
So far x property of object is:  1
After firest an = an.party()

Before second an = an.party()
So far x property of object is:  2
After second an = an.party()

Before third an = an.party()
So far x property of object is:  3
After third an = an.party()

Before one more party()
So far x property of object is:  4
After one more party()
>>> 
=============== RESTART: /home/user/EDIBO/Python/OOP_test_1.py ===============

Before an = PartyAnimal()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/EDIBO/Python/OOP_test_1.py', 'PartyAnimal': <class '__main__.PartyAnimal'>}
After an = PartyAnimal()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/EDIBO/Python/OOP_test_1.py', 'PartyAnimal': <class '__main__.PartyAnimal'>, 'an': <__main__.PartyAnimal object at 0x7f78d0002668>}

Before first an = an.party()
So far x property of object is:  1
After first an = an.party()

Before second an = an.party()
So far x property of object is:  101
After second an = an.party()

Before third an = an.party()
So far x property of object is:  102
After third an = an.party()

Before one more party()
So far x property of object is:  103
After one more party()
>>> vars(an)
{'x': 103}
>>> 
=============== RESTART: /home/user/EDIBO/Python/OOP_test_1.py ===============

Before an = PartyAnimal()
After an = PartyAnimal()

Before first an = an.party()
So far x property of object is:  1
After first an = an.party()

Before second an = an.party()
So far x property of object is:  101
After second an = an.party()

Before third an = an.party()
So far x property of object is:  201
After third an = an.party()

Before one more party()
So far x property of object is:  202
After one more party()
>>> 
=============== RESTART: /home/user/EDIBO/Python/OOP_test_1.py ===============

Before an = PartyAnimal()
Traceback (most recent call last):
  File "/home/user/EDIBO/Python/OOP_test_1.py", line 17, in <module>
    an2 = PartyAnima()
NameError: name 'PartyAnima' is not defined
>>> 
=============== RESTART: /home/user/EDIBO/Python/OOP_test_1.py ===============

Before an = PartyAnimal()
After an = PartyAnimal()

Before first an = an.party()
So far x property of object is:  1
After first an = an.party()

Before second an = an.party()
So far x property of object is:  101
After second an = an.party()

Before third an = an.party()
So far x property of object is:  201
After third an = an.party()

Before one more party()
So far x property of object is:  202
After one more party()
>>> 
=============== RESTART: /home/user/EDIBO/Python/OOP_test_1.py ===============

Before an = PartyAnimal()
After an = PartyAnimal()

Before first an = an.party()
So far x property of object is:  1
After first an = an.party()
Traceback (most recent call last):
  File "/home/user/EDIBO/Python/OOP_test_1.py", line 32, in <module>
    an._init_()
AttributeError: 'PartyAnimal' object has no attribute '_init_'
>>> 
=============== RESTART: /home/user/EDIBO/Python/OOP_test_1.py ===============

Before an = PartyAnimal()
After an = PartyAnimal()

Before first an = an.party()
So far x property of object is:  1
After first an = an.party()
Ī am constructed

Before second an = an.party()
So far x property of object is:  1
After second an = an.party()

Before third an = an.party()
So far x property of object is:  201
After third an = an.party()

Before one more party()
So far x property of object is:  202
After one more party()
>>> 
=============== RESTART: /home/user/EDIBO/Python/OOP_test_1.py ===============

Before an = PartyAnimal()
After an = PartyAnimal()
{}

Before first an = an.party()
So far x property of object is:  1
After first an = an.party()
Ī am destructed 100

Before second an = an.party()
So far x property of object is:  101
After second an = an.party()

Before third an = an.party()
So far x property of object is:  201
After third an = an.party()

Before one more party()
So far x property of object is:  202
After one more party()
>>> an
<__main__.PartyAnimal object at 0x7f2cb9450630>
>>> vars(an)
{'x': 202}
>>> type(an)
<class '__main__.PartyAnimal'>
>>> an._del_
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    an._del_
AttributeError: 'PartyAnimal' object has no attribute '_del_'
>>> an._del_()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    an._del_()
AttributeError: 'PartyAnimal' object has no attribute '_del_'
>>> an.__del__()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    an.__del__()
AttributeError: 'PartyAnimal' object has no attribute '__del__'
>>> an.__del__()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    an.__del__()
AttributeError: 'PartyAnimal' object has no attribute '__del__'
>>> an._del_()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    an._del_()
AttributeError: 'PartyAnimal' object has no attribute '_del_'
>>> an.__del__()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    an.__del__()
AttributeError: 'PartyAnimal' object has no attribute '__del__'
>>> an = 900
>>> vars(an)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    vars(an)
TypeError: vars() argument must have __dict__ attribute
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/EDIBO/Python/OOP_test_1.py', 'PartyAnimal': <class '__main__.PartyAnimal'>, 'an': 900}
>>> an.__del__()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    an.__del__()
AttributeError: 'int' object has no attribute '__del__'
>>> an
900
>>> an = 900
>>> 
=============== RESTART: /home/user/EDIBO/Python/OOP_test_1.py ===============

Before an = PartyAnimal()
After an = PartyAnimal()
{}

Before first an = an.party()
So far x property of object is:  1
After first an = an.party()
Ī am constructed

Before second an = an.party()
So far x property of object is:  1
After second an = an.party()

Before third an = an.party()
So far x property of object is:  201
After third an = an.party()

Before one more party()
So far x property of object is:  202
After one more party()
>>> an
<__main__.PartyAnimal object at 0x7fbf6329e668>
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/EDIBO/Python/OOP_test_1.py', 'PartyAnimal': <class '__main__.PartyAnimal'>, 'an': <__main__.PartyAnimal object at 0x7fbf6329e668>}
>>> vars(an)
{'x': 202}
>>> dir(an)
['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_init_', 'party', 'x']
>>> 
