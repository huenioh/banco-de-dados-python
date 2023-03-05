def validate_cpf(cpf):
    # Remove qualquer caractere que não seja um dígito da string de entrada
    cpf = ''.join(filter(str.isdigit, cpf))

    # Se o comprimento da string não for 11 após remover os caracteres que não são dígitos, é inválido
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (por exemplo, '00000000000', '11111111111')
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += (10 - i) * int(cpf[i])
    digito1 = 11 - (soma % 11)
    if digito1 == 10 or digito1 == 11:
        digito1 = 0

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += (11 - i) * int(cpf[i])
    digito2 = 11 - (soma % 11)
    if digito2 == 10 or digito2 == 11:
        digito2 = 0

    # Se os dígitos verificadores calculados coincidirem com os dígitos de entrada, o CPF é válido
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False