'''de la tastatura se citesc patru cuvinte fiecare cuvant fiind citit intro singu
ra variabila. Elaborati un program care va forma o fraza,va include
toate cuvintele in sir.Fiecare cuvant va fi despartit prin spatiu
Ultimul caracter din fraza va fi semnul punct
la ecran se vor afisa cuvintele citite cat si fraza formata'''

a=str(input('primul cuvant este: '))
b=str(input('al doilea cuvant este: '))
c=str(input('al treilea cuvant este: '))
d=str(input('al patrulea cuvant este: '))
s=a+" "+b+" "+c+" "+d+"."
print('primul cuvant citit este: ',a)
print('al doilea cuvant citit este: ',b)
print('al treilea cuvant citit este: ',c)
print('al patrulea cuvant citit este: ',d)
print('fraza este: ',s)
