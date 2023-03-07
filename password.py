import random
caracteres = [chr(i) for i in range (33, 127)]
caracteres_aleatorios = random.sample(caracteres, 10)
senha = "" .join(caracteres_aleatorios)
print(f"Nova senha gerada: {senha}")