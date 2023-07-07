user_point = 0    
pc_point = 0

for count in range (0,5):
    from random import randint
    num_pc = randint(0,10)
    par_impar = input("Escolha entre par ou impar. P ou I\n")
    while par_impar != "P" and par_impar != "I":
        par_impar = input("Entrada invalida. Escolha entre par ou impar. P ou I\n")
        
    num_user = int(input("Escolha um numero entre 0 e 10\n"))
    
    sum = num_user + num_pc
    
    print (f"A soma do numero do usuario e numero do pc foi de {sum}")
    
    if (par_impar == "P" ) and (sum % 2 == 0):
        user_point = user_point +1
        print("O usuario ganhou")
    elif (par_impar == "P") and (sum % 2 != 0):
        pc_point = pc_point + 1
        print("O PC ganhou.")
    elif (par_impar == "I") and (sum % 2 == 0):
        pc_point = pc_point + 1
        print("O PC ganhou")
    elif (par_impar == "I") and (sum % 2 != 0):
        user_point = user_point +1
        print("O usuario ganhou")

    
    #mostrar placar
if user_point > pc_point:
    print(f"O placar final foi de: \nUsuario {user_point} pontos. \n PC {pc_point} pontos. \n O usuario ganhou. ")
else:
    print(f"O placar final foi de: \nUsuario {user_point} pontos. \n PC {pc_point} pontos. \n O PC ganhou. ")
