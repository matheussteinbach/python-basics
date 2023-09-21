print(12) # (argumento)

print(12,34) # dois argumentos ou mais separados por vírgula, argumentos não nomeados

print(56,78, sep='-') # argumento nomeado sep -> modifica o separador 

# \r\n (return)(linefeed) -> quebra de linha CRLF
# \n -> LF (Linux,Mac) 

print('\njoao')
print('\n',1234,sep='',end='##') # argumento nomeado end -> modifica o final (padrão quebra de linha)
print('cleiton')

# nos argumentos nomeados sep e end, é possivel adicionar caracteres ou quebrar linhas