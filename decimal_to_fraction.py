def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def decimal_to_fraction(decimal_str):
    decimal_str = decimal_str.replace(',', '.')

    if '.' not in decimal_str:
        return f"The input '{decimal_str}' is not valid."

    integer_part, decimal_part = decimal_str.split('.')
    num_decimal_digits = len(decimal_part)

    numerator = int(integer_part + decimal_part) - int(integer_part)
    denominator = 10 ** num_decimal_digits - 1

    # Simplifica a fração o máximo possível
    divisor = gcd(numerator, denominator)
    simplified_numerator = numerator // divisor
    simplified_denominator = denominator // divisor

    return f"A fração geratriz da dízima {decimal_str} é: {simplified_numerator}/{simplified_denominator}"

# Recebe o input do usuário
user_input = input("Digite uma dízima: ")

# Calcula a fração geratriz e imprime o resultado
fraction_result = decimal_to_fraction(user_input)
print(fraction_result)
print('')
input("Pressione Enter para sair...")
