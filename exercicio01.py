lista_compras = []
item = 0
option = input("Deseja incluir itens na lista de compras?\n")

if option == "sim":
    while item != "fim":
        item = input("Informe o item a adicionar à lista:\n")
        lista_compras.append (item)
    else:
        lista_compras.pop(-1)
        print(lista_compras)