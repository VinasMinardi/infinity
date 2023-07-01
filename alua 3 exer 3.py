recebe = 0
filho_plus_3 = 0

for count in range(0,5):
    salario = float(input("Informe o seu salario:\n"))
    num_filhos = int(input("Informe o numero de filhos:\n"))

    if salario <= 1200:
        recebe = recebe + 1
     
    if num_filhos > 3:
        filho_plus_3 = filho_plus_3 + 1

print (recebe)
print (filho_plus_3)