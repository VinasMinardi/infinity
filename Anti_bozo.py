candidato_1 = 0
candidato_2 = 0
branco = 0
nulo = 0

email = str(input("Digite o e-mail. para cadastro."))
password = input("Digite uma senha para cadastro.")

for count in range (1,4):

    voto = input(" Digite o nome do seu candidato.\n As opções são Lula, Bolsonaro. Paravoto em branco digite Branco. \nQualquer outra entrada diferente será considerada nula. \n")

    if voto == "Lula":
        candidato_1 = candidato_1 + 1
    elif voto == "Bolsonaro":
        candidato_2 = candidato_2 + 1
    elif voto == "Branco":
        branco = branco + 1
    else:
        nulo = nulo + 1


percentual_1 = (candidato_1 * 100) / count
percentual_2 = (candidato_2 * 100) / count
percentual_bran = (branco * 100) / count
percentual_nulo = (nulo * 100) / count


password2 = input("Digite sua senha cadastrada.")

while password2 != password:
    password2 = input("Senha incorreta. Digite novamente")

if password2 == password: 
    print (f"O total de votos foi de {count} \n O resultado da eleição foi: \n Lula com {percentual_1} % dos votos \n Bolsonaro com {percentual_2} % dos votos. \n {percentual_bran} % de votos em branco. \n {percentual_nulo} % de votos nulos. ")
    if percentual_1 > percentual_2:
        print("Lula eleito.")
    elif percentual_2 >percentual_1:
        print("Bolsonaro eleito")
    elif percentual_1 == percentual_2:
        print("Segundo turno.")  
        