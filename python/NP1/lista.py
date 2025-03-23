#primeiro exemplo
x = 1 
print('inicio')
while x < 10 :
    print(x)
    x = x + 1
print('FIm')

print(x) 

#segundo exemplo
x = 10
print('inicio')
while x < 10 :
    print(x)
    x = x + 1
print('FIm')

#terceiro exemplo
x = 10 

while x < 10 :
    print(x)
    x= x+1
print("fim")


#quarto exemplo

x = 1
while x < 10 :
    print(x)

    if x == 5:
        break
    x = x + 1
print('fim')



#quinto

x = 1 

while x < 10:
    x = x + 1
    if x <= 5:
        continue
    print(x)

print('fim')

#sexto

x = 1 
while x < 10:
    if x <= 5:
    #logo sera implementado 
    #algo aqui 
        pass
    else:
        print('print else')
    print(x)
    x = x + 1

#setimo

x = 0 
for x in [1, 6, 3, 1, 4]:
    pass
print(x)

#oitavo

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print('Variavel: ', i)
print('fim')



#oitavo.1

for i in range(1,11):
    print('Variavel: ', i)
print('fim')



#nove

for i in [2, 5, 3, 4]:
    print(i)

#10

for c in ['p', 'y', 't', 'h', 'o', 'n']:
    print(c)


#11

#X = list(range(1, 11))
#for i in X:
#    print('Variavel: ', i)
#print(sum(x))

#12

print (list(range(7)))
print (list(range(2, 6)))
print (list(range(11, 5)))
print (list(range(11,30,3)))
print (list(range(10,1,-2)))


print()