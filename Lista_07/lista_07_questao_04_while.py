texto = input('Informe algo: ')

vogais = 'aeiouAEIOUãõÃÕáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛäëïöüÄËÏÖÜ'
consoantes = 'qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZXCVBNMñÑ'
numeros = '0123456789'

contador_vogais = 0
contador_numeros = 0
contador_consoantes = 0
contador_outros = 0
qt_letras = 0
posicao = 0

# Obtendo a quantidade de caracteres
for letra in texto: 
  qt_letras += 1

# Identificando o caractere
while posicao < qt_letras:
    if (texto[posicao] in vogais):
      contador_vogais += 1
    elif (texto[posicao] in consoantes):
      contador_consoantes += 1
    elif (texto[posicao] in numeros):
      contador_numeros += 1
    else:
      contador_outros += 1
    posicao += 1

print('A quantidade de Vogais é {0}'.format(contador_vogais))
print('A quantidade de Consoantes é {0}'.format(contador_consoantes))
print('A quantidade de Números é {0}'.format(contador_numeros))
print('A quantidade de Outros Caracteres é {0}'.format(contador_outros))