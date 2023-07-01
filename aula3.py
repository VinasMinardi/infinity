

for nome in range(0,3):
    nome = input("Informe seu nome\n")
    valor_veiculo = float(input("Informe o valor do veiculo.\n"))
    salario = float(input('Informe o seu rendimento mensal.\n'))
    num_parcela = int(input('Informe a quantidade de parcelas.\n'))

    parcela = valor_veiculo / num_parcela
    print ('O valor da sua parcela seria de ', parcela, 'reais mensais.')

    max_parcela = salario * 0.3
    print ("Sua parcela maxima de acordo com seu salario seria de ", max_parcela, "reais mensais.")

    if (parcela > max_parcela):
        print ('O valor da parcela do seu veiculo supera o maximo aprovado para seu sálario')
    else:
        print("O seu emprestimo foi aprovado")