# Составте генератор (yield), который преобразует все буквенные символы в заглавные

def uppercase_transform(char):
    return char.upper() if char.isalpha() else char


def uppercase_generator(input_string):
    return map(uppercase_transform, input_string)


input_str = "Hello, World!"
result = ''.join(uppercase_generator(input_str))
print(result)
