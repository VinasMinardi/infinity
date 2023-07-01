print ("Vamos solicitar agora 6 numeros inteiros e apresentar a soma total dos numeros, e de todos os numeros pares")
sum = 0
sum2 = 0
for count in range(0,6):
    num = int(input("Digite um numero."))
    sum = (sum + num)
    if num % 2  == 0:
        sum2 = sum2 + num

print (f"A soma total é de {sum}")
print (f"A soma dos numeros pares é de {sum2}")