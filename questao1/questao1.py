linhas = []
n = int(input())

if not isinstance(n, int):
    raise ValueError("Numero de linhas deve ser um inteiro")
elif n > 50:
    raise ValueError("Cada teste só pode ter até 50 strings")
elif n < 1:
    raise ValueError("Cada teste deve ter ao menos 1 string")

for idx in range(n):
    frase = input()

    if len(frase) > 50:
        raise ValueError("String excede 50 caracteres: %s" % frase)
    else:
        linhas.append( frase )

for linha in linhas:

    ordenadas = sorted(linha.split(), key=len)

    for palavra in ordenadas: print(palavra+" ", end="")