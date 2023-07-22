lista_compras = []
item = 0
option = input("Deseja incluir itens na lista de compras?\n")

if option == "sim":
    while item != "fim":
        item = input("Informe o item a adicionar à lista:\n")
        lista_compras.append (item)
    else:
        lista_compras.pop(-1)

option_2 = input(f"Essa é sua lista.\n {lista_compras} \nDeseja excluir algum item?\n")



if option_2 == "sim":
    remove = input ("Qual item deseja remover?:\n")
    
    while remove != "fim":
        lista_compras.remove(remove)
        remove = input ("Qual item deseja remover?:\n")
        if remove in lista_compras:
           lista_compras.remove(remove) 
    else:
        print(lista_compras)

else:
    print("Ok, essa é sua lista final")
    print(lista_compras)