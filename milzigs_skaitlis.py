#! /usr/bin/python3.6

print("Ievadiet skaitli")
# a=2**20000000

#te ir tris darbibas - vertibas sagaidsana, vertibas parveidosana, pieskirsana
#argument = input()
#a = int(argument)

#pildot in(input()) "bez izmeginajuma" programma var vienkrasi izlidot ...
#tapec lai "nelidotu"mes izmantosim  try ... except ... finally konstrukciju
paziime = False
while (not paziime):
#while pazime==False:
#while pazime!=True:
   try:
      a = int( input() )
      paziime = True
   except:
      print("Diemzel, cienimajais lietotajs, to kas ievadits, nevar parveido par vesela tipa skaitli :-( ")
      print("Ludzu,ievadi skaitli velreiz")

#if (a == int): print("a**100")
#ja jau loti gribas, tad var salidzinat type(a) == int -> rezultats bus True
if (a == 5):
   print(a**100)
   print("Aprēķins ir gatavs")
   print("Sis teksts atrodas arpus blok - pierakstits bez atsparpem prieksa, tapec tas paradisies jebkura gadijuma")
#print (Ievadāmi vērtībai jābūt skaitlim")
#b=a**100
