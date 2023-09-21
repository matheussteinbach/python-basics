# Operadores Aritméticos 

adicao = 10 + 10.2
print('Adição:',adicao) # int + float sempre = float

subtracao = 10 - 5
print('Subtração:',subtracao)

multiplicacao = 10 * 10
print('Multiplicação:',multiplicacao)

# Se tiver float na conta, sempre retornará float
divisao = 10 / 2.2  # sempre retorna float
print('Divisão:',divisao) 
div1 = 10/2
print(div1)

divisao_inteira = 10 // 2 # int
print('Divisão inteira:',divisao_inteira)
div = 10 // 2.2
print(div) 

exponenciacao = 2 ** 10
print('Exponenciação:',exponenciacao)

# Resto da divisão -> módulo
modulo = 55 % 2
print('Resto da divisão:',modulo)

# Concatenação -> Junção de strings
concatenacao = 'A' + 'B' + 'C'
print(concatenacao)
conc = 'Matheus'+ ' ' + 'Steinbach'
print(conc)

# Repetição -> Multiplicação da string
repeticao = 'Matheus' * 10
print(repeticao)

'''
Precedencia dos Operadores
1 - ()
2 - **
3 - * , / , // , %
4 - + , -
'''
print( 1+1 ** 5+5)
print((1+1) ** (5+5))