renas = dict()
num_testes = int(input())
teste_atual = 1

if num_testes > 10000: raise ValueError("Numero de casos teste excede 10.000")
elif num_testes < 1: raise ValueError("Numero de casos teste menor que 1")

def teste():
    params = str(input()).split()
    if len(params) != 2: raise ValueError("Parametros do teste precisam ser dois inteiros: m n")
    
    total_renas = int(params[0])
    renas_treno = int(params[1])

    if total_renas < 5: raise ValueError("Parametro 1 deve ser no minimo 5 renas")
    if total_renas > 1000: raise ValueError("Parametro 1 deve ser no maximo 1.000 renas")
    if renas_treno < 5: raise ValueError("Parametro 2 deve ser no minimo 5 renas")
    if renas_treno > 1000: raise ValueError("Parametro 2 deve ser no maximo 1.000 renas")

    for _ in range(total_renas):
        rena = str(input()).split()
        _nome, _peso, _idade, _altura = rena

        try:_peso = int(_peso)
        except: raise ValueError("Peso da rena %s deve ser um inteiro" % _nome)
        try:_idade = int(_idade)
        except: raise ValueError("Idade da rena %s deve ser um inteiro" % _nome)
        try:_altura = float(_altura)
        except: raise ValueError("Altura da rena %s deve ser um ponto flutante" % _nome)

        if _peso < 1 or _peso > 300: raise ValueError("Peso da rena %s deve ser entre 1 e 300" % _nome)
        if _idade < 1 or _idade > 300: raise ValueError("Idade da rena %s deve ser entre 1 e 300" % _nome)
        if _altura < 0.0 or _altura > 3.0: raise ValueError("Altura da rena %s deve ser entre 0.00 e 3.00" % _nome)

        renas[_nome] = {"nome":_nome, "peso":_peso, "idade":_idade, "altura":_altura}

    print("CENARIO {%d}" % teste_atual)

    resultado = []

    sort_por_peso = sorted(renas.items(), key=lambda r: r[1]["peso"], reverse=True)

    categorias_de_peso = {}
    for r in sort_por_peso:
        peso = r[1]["peso"]
        if peso in categorias_de_peso: categorias_de_peso[peso].append(r)
        else: categorias_de_peso[peso] = [r]

    for categoria_peso in categorias_de_peso:
        sort_categoria_peso = sorted(categorias_de_peso[categoria_peso], key=lambda r: r[1]["idade"])

        categorias_de_idade = {}
        for r in sort_categoria_peso:
            idade = r[1]["idade"]
            if idade in categorias_de_idade: categorias_de_idade[idade].append(r)
            else: categorias_de_idade[idade] = [r]

        for categoria_idade in categorias_de_idade:
            sort_categoria_idade = sorted(categorias_de_idade[categoria_idade], key=lambda r: r[1]["nome"])
            for r in sort_categoria_idade: resultado.append(r)

    for idx in range(renas_treno):
        print("%d - %s" % (idx + 1, resultado[idx][0]))

while(teste_atual <= num_testes):
    teste()
    teste_atual = teste_atual + 1
