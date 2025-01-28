frase=input('Digite uma frase:')
cont=0
for i in frase:
    if i in 'aeiou' or i in 'AEIOU':
        cont+=1
print(cont)

