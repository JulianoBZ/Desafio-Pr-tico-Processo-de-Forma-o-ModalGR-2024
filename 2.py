from datetime import datetime

#Lendo arquivo de texto
f = open("funcionarios.txt", "r")

#Separando cada dado em um array
geral = []
geral = (f.read()).split("|")

#Separando os dados de cada funcionário em um array para ser inserido em outro
contador = 0
arr_total = []
arr_indv = []
reading = True

while reading:
    if len(geral) < contador+1:
        reading = False
    else:
        arr_indv.append(geral[contador])
        contador += 1
        if len(arr_indv) == 3:
            arr_total.append(arr_indv)
            arr_indv = []

#Com esse grande array organizado, verificar a terceira posição em cada array, dentro do array arr_total para ver a data

mes_atual = datetime.now().month
arr_niver = []

for each in arr_total:
    mes = datetime.strptime(each[2], '%d/%m/%Y').month
    if mes == mes_atual:
        arr_niver.append(each)

#Abrindo arquivo
f2 = open("aniversariantes_do_mes.txt", "w")

#Arrays adicionados, printando e escrevendo no arquivo
for each in arr_niver:
    print(each[0],',',each[1],',',each[2])
    f2.write(str(each[0]+','+each[1]+','+each[2]))



