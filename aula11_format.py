# Format
# Função - método(dentro do objeto string)

a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={:.2f}'.format(a,b,c)
print(formato)

formato2 = 'a={0} a={0} b={1} a={0} c={2:.2f}'.format(a,b,c) # index 0,1,2
print(formato2)

formato3 = 'a={0} b={1} c={nome3:.2f}'.format(a,b,nome3=c) #ao nomear um index todos dps tem que ser nomeados
print(formato3)

formato4 = 'a={nome1} b={nome2} c={nome3:.2f}'.format(nome1=a,nome2=b,nome3=c) #ao nomear um index todos dps tem que ser nomeados
print(formato4)