# Conversão de tipos, coerção
'''
Nomes: type convertion, typecasting, coercion

- Ato de converter um tipo em outro tipo

Tipos imutaveis e primitivos: str, int, float, bool
# Imutavel não consegue alterar no programa depois de criar
# Primitivos - tipos literais que consegue escrever no programa
'''

# Mesmo operador pra fazer coisas diferentes -> polimorfismo
# coisas diferentes = somar int e somar str (concatenar)

print(1+1) # somar
print('a'+'b') # concatenação

# Impossivel somar dois tipos diferentes - erro
#print('1'+ 1)

# int() - função(classe) de conversão de tipo para inteiro

print('1',type('1'))
print(type(int('1')))

print(int('1')+ 1)

# float() - conversão para float

print(float('1') + 1) # Python consegue somar int com float - retorna outro float

# bool() - conversão para booleana
# vazia = False, com valor qualquer = True 

print(bool(''))
print(bool(' '))

# str() - conversão para string
# print(11+'b') - fica ambíguo, não sabe se quer somar ou concatenar 

print(str(11) + 'b')