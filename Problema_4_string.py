'''de la tastatura se citesc
patru cuvinte fiecare cuvant fiind citit
intro singura variabila,un cuvant va fi format din minim 3 caractere
elaborati un program care va forma un cuvant nou in felul urmator:
din primul cuvant va adauga primele 2 caractere
din al doilea cuvant va adauga primul caracter
se vor adauga primele trei caractere din cuvantul al treilea
se vor adauga n/2 al patrulea cuvant
la ecran se vor afisa cuvintele citite cat si cel format'''

a=str(input('primul cuvant este: '))
b=str(input('al doilea cuvant este: '))
c=str(input('al treilea cuvant este: '))
d=str(input('al patrulea cuvant este '))
if ((len(a)<3) or (len(b)<3) or (len(c)<3) or (len(d)<3)):
    print('nu corespunde conditiei')
else:
    x=a[:2]
    y=b[:1]
    z=c[:3]
    len1=((len(d))//2)
    len2=len1
    w=d[:len2]

    print('Primul cuvant citit este: ',a)
    print('Al doilea cuvant citit este: ',b)
    print('Al treilea cuvant citit este: ',c)
    print('Al patrulea cuvant citit este: ',d)
    cuvantul=x+y+z+w
    print('Cuvantul format este = ',cuvantul)
