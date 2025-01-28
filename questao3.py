nota1=float(input('Digite sua primeira nota: '))
peso1=float(input('Digite o peso da primeira nota: '))
nota2=float(input('Digite sua segunda nota: '))
peso2=float(input('Digite o peso da segunda nota: '))

media_ponderada=(nota1*peso1+nota2*peso2) / (peso1+peso2)
print(media_ponderada)