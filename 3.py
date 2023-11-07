def emprestimo():
    #Definindo variáveis
    emprestimo = 0
    salario = 0
    notas = {
        "notas_100":0,
        "notas_50":0,
        "notas_20":0,
        "notas_10":0,
        "notas_5":0,
        "notas_2":0,
        }
    anos = int(input("Quantos anos empregado na empresa?: "))
    
    validando = True

    if anos < 5:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        return
    
    salario = int(input("Qual o valor do seu salário atual? :"))
    while validando:
        emprestimo = int(input("Qual o valor do empréstimo desejado?: "))
        if (emprestimo > salario*2) or (emprestimo % 2 != 0) :
            print("Insira um valor válido!")
        else:
            validando = False

    validando = True
    tipo = 0

    #Validando o tipo de notas a ser cobrado
    while validando:
        tipo = int(input("Deseja o saque em NOTAS ALTAS (1), NOTAS BAIXAS (2) ou NOTAS MEIO A MEIO (3)? : "))
        if tipo == 1 or tipo == 2 or tipo == 3:
            validando = False
        else:
            print("Insira um valor válido!")

    match tipo:
        case 1:
            v_100 = emprestimo // 100
            emprestimo = emprestimo - (v_100*100)
            notas["notas_100"] = v_100
            v_50 = emprestimo // 50
            emprestimo = emprestimo - (v_50*50)
            notas["notas_50"] = v_50
            v_20 = emprestimo // 20
            emprestimo = emprestimo - (v_20*20)
            notas["notas_20"] = v_20
            v_10 = emprestimo // 10
            emprestimo = emprestimo - (v_10*10)
            notas["notas_10"] = v_10
            v_5 = emprestimo // 5
            emprestimo = emprestimo - (v_5*5)
            notas["notas_5"] = v_5
            v_2 = emprestimo // 2
            emprestimo = emprestimo - (v_2*2)
            notas["notas_2"] = v_2
        case 2:
            v_20 = emprestimo // 20
            emprestimo = emprestimo - (v_20*20)
            notas["notas_20"] = v_20
            v_10 = emprestimo // 10
            emprestimo = emprestimo - (v_10*10)
            notas["notas_10"] = v_10
            v_5 = emprestimo // 5
            emprestimo = emprestimo - (v_5*5)
            notas["notas_5"] = v_5
            v_2 = emprestimo // 2
            emprestimo = emprestimo - (v_2*2)
            notas["notas_2"] = v_2

        #No exemplo do "notas meio a meio" no arquivo, foi utilizado o método "notas altas" além de usar um número ímpar como empréstimo, por favor corrigir ou desconsiderar esta questão
        case 3:

            emprestimo_alto = emprestimo / 2
            emprestimo_baixo = emprestimo / 2

            v_100 = emprestimo_alto // 100
            emprestimo_alto = emprestimo_alto - (v_100*100)
            notas["notas_100"] = v_100
            v_50 = emprestimo_alto // 50
            emprestimo_alto = emprestimo_alto - (v_50*50)
            notas["notas_50"] = v_50

            #somando o resto do emprestimo de notas altas
            emprestimo_baixo += emprestimo_alto

            v_20 = emprestimo_baixo // 20
            emprestimo_baixo = emprestimo_baixo - (v_20*20)
            notas["notas_20"] = v_20
            v_10 = emprestimo_baixo // 10
            emprestimo_baixo = emprestimo_baixo - (v_10*10)
            notas["notas_10"] = v_10
            v_5 = emprestimo_baixo // 5
            emprestimo_baixo = emprestimo_baixo - (v_5*5)
            notas["notas_5"] = v_5
            v_2 = emprestimo_baixo // 2
            emprestimo_baixo = emprestimo_baixo - (v_2*2)
            notas["notas_2"] = v_2


    #Printando o resultado
    print("Notas do empréstimo: ")

    print( " ",notas["notas_100"],"x100 \n",
           notas["notas_50"],"x50 \n",
           notas["notas_20"],"x20 \n",
           notas["notas_10"],"x10 \n",
           notas["notas_5"],"x5 \n",
           notas["notas_2"],"x2 \n"
    )

    return
            
#Chamando função
emprestimo()