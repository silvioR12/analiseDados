"""
Autor: Silvio Lopes
Dados para análise : Portal transparência governo federal
02/11/2022
"""

import pandas as pd

#criando lista de valores numéricos para coluna de valor transferido 1 semestre 2022
ListaNum = []
ListaNum2 = []
#Lendo o arquivo que está contido as informações 2022
arquivo = pd.read_csv('arquivo1.csv',sep = ';')
arquivo2 = pd.read_csv('arquivo2.csv',sep = ';')
#Pegando apenas a coluna de valor transferido
valor = arquivo.iloc[:,1]
valor2 = arquivo2.iloc[:,1]
#Transformando valores de uma coluna para uma lista, para melhor análise
valorSTR = list(valor)
valorSTR2 = list(valor2)

#Pegando valores inteiros da lista

for x in valorSTR:
    ListaNum.append(int(x))
    
for x in valorSTR2:
    ListaNum2.append(int(x))

    Total_1semestre_Bolsa = sum(ListaNum2)

Total_1semestre_Aux = sum(ListaNum)

print('O total gastos no 1 semestre de 2022 do Auxílio Brasil foi de R${:,}'.format(Total_1semestre_Aux))
print('O total gastos no 1 semestre de 2021 do bolsa  família foi de R${:,}'.format(Total_1semestre_Bolsa))

if Total_1semestre_Bolsa > Total_1semestre_Aux:
    programa_social = 'Bolsa família'
    diferenca = Total_1semestre_Bolsa - Total_1semestre_Aux
else:
    programa_social = 'Auxílio Brasil'
    diferenca = Total_1semestre_Aux - Total_1semestre_Bolsa
    
print('\nA diferença entre os dois programais sociais no 1 semestre foi de R${:,} a mais pro {}'.format(diferenca,programa_social))
