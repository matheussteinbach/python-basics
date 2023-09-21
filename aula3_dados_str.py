#Tipos de dados do Python
'''
Tipo de tipagem do python -> Dinâmica  / Forte
tipagem dinâmica: reconhece o tipo de dado informado
        estática: é necessário informar
tipagem forte: não realiza conversões de tipo automaticamente (ex: int pra str)
        fraca: realiza
https://www.treinaweb.com.br/blog/quais-as-diferencas-entre-tipagens-estatica-ou-dinamica-e-forte-ou-fraca
        
str -> string -> texto
Strings - textos dentro de aspas simples/duplas

'''
print(123) # python reconhece como número inteiro

print('Matheus')
print("Matheus Steinbach")
print('Matheus "Steinbach"')

# Caractere de Escape \
# Não é considerado pelo interpretador, conta o " como caractere
print("Matheus \"Steinbach\"")

# r antes -> mostra o caractere de escape
# utilizado para expressões regulares
print(r"Matheus \"Steinbach\"")