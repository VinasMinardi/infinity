ageup = 0
sumage = 0
maxage = 0
nameold = "Empty"

for name in range(0,5):
    name = input("Digite seu nome:\n")
    age = int(input("Digite sua idade:\n"))
    sex = input('Digite o seu sexo: \n')
    if maxage < age:
        maxage = 0 + age 
        nameold = name
     
    sumage = sumage + age
    

    if (age < 30): 
        ageup = ageup+1
medage = sumage / 5 
print (f"A media das idades é de {medage} anos.")
print (f"Existem {ageup} pessoas com mais de 30 anos.")
print (f'A pessoa mais velha é {nameold} com {maxage}')
