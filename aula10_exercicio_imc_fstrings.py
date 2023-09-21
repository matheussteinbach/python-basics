nome = 'Matheus'
altura = 1.83
peso = 79
imc = peso / (altura ** 2) 
# print(...) <- place holder

print(nome,'tem',altura,'de altura, pesa',peso,'quilos e seu IMC é',imc)
#print(round(imc,2)) -> arredondar com 2 casas após a virgula


# f - strings
# f antes das aspas habilita a formatação. {} nas variaveis
# formatação de casal decimal = :.numerof
print(f'{nome} tem {altura:.3f} de altura, pesa {peso} quilos e seu IMC é {imc:.4f}')


num = 100000
print(f'{num:,}') # ,. coloca a separação por vírgulas 
print(f'{num:,.2f}')