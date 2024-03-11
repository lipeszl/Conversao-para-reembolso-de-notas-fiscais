from num2words import num2words

def numero_por_extenso(numero):
    # Separar a parte inteira e decimal
    parte_inteira, parte_decimal = numero.split(',')
    
    # Converter a parte inteira para extenso
    parte_inteira_extenso = num2words(int(parte_inteira), lang='pt_BR')
    if parte_inteira_extenso.endswith(' e zero'):
        parte_inteira_extenso = parte_inteira_extenso[:-len(' e zero')]
    
    # Converter a parte decimal para extenso
    parte_decimal_extenso = num2words(int(parte_decimal), lang='pt_BR')
    if parte_decimal_extenso.endswith(' e zero'):
        parte_decimal_extenso = parte_decimal_extenso[:-len(' e zero')]
    
    return f'{parte_inteira_extenso} reais e {parte_decimal_extenso} centavos'

def converter_para_extenso(entrada):
    partes = entrada.split()
    saida = ""
    i = 0
    while i < len(partes):
        if ',' in partes[i]:
            numero_extenso = numero_por_extenso(partes[i])
            saida += f'{partes[i-2]} {partes[i-1]} {partes[i]} ({numero_extenso})\n\n'
            i += 1  # Avançar para a próxima palavra
        else:
            saida += partes[i] + " "
            i += 1  # Avançar para a próxima palavra
    return saida.strip()

entrada = input("Digite os dados: ")
saida = converter_para_extenso(entrada)
if saida:
    print(saida)
else:
    print("Nenhum número decimal encontrado na entrada.")