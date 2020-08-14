class PartyAnimal:
   x = 0

#_init_metode tiks izpildita tikai vienu reizi, veidojot (katru) instanci
   
   def _init_(self):
    print('Ī am constructed')
    self.x = 0
    
   def party(self) :
     self.x = self.x + 1
     print("So far x property of object",\
           "is: ",self.x)

   def __del__(self):
    print('Ī am destructed', self.x)
    
print("\nBefore an = PartyAnimal()")
#print(vars())
an = PartyAnimal()
print("After an = PartyAnimal()")
#print(vars())
#print("an data type or class: ", type(an))
#print("an methods and properties: ", dir(an))
#print("an x property data type: ", type(an.x))
#print("an party method data type: ", type(an.party))
#print(vars(an)) # objekts tiaki izveidots {}?
print(vars(an))
#tikai ja klase ir ar _ini_ in ar self.x
#tikai tad tad {'x': 0}, savadak ir {}

print("\nBefore first an = an.party()")
an.party()
print("After first an = an.party()")
#print(vars(an)) # objekts "aiztikts" {'x': 1}

an.x = 100
an._init_()

print("\nBefore second an = an.party()")
an.party()
print("After second an = an.party()")

an.x = 200

print("\nBefore third an = an.party()")
an.party()
print("After third an = an.party()")

print("\nBefore one more party()")
PartyAnimal.party(an)
print("After one more party()")

# Code: http://www.py4e.com/code3/party2.py
