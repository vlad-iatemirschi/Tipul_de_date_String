'''
Se citeste un sir de caractere care reprezinta CNP-ul unei persoane. Sa se verifice corectitudinea lui:numarul de caractere sa fie 13 si toate
caracterele sa fie cifre.
'''
p=input('introduceti CNP: ')
n=0
if (len(p)<13)or(len(p)>13):
    print('CNP este fals')
else:
    for i in p:
        if ord(i) in range(48,58):
            n+=1
    if n==13:
        print('CNP este adevarat')
    else:
        print('CNP este fals')