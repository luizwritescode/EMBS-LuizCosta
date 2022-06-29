num_testes = int(input())
teste_atual = 1

if num_testes < 1: raise ValueError("Numero de casos testes nao pode ser menor que 1")

testes = []

for _ in range(num_testes):
    p1, p2 = str(input()).split()
    testes.append([p1,p2])

def teste(p1,p2):
    
    if len(p1) < 1 or len(p1) > 50: raise ValueError("Palavra 1 do teste %d deve ter entre 1 e 50 caracteres" % teste_atual)
    if len(p2) < 1 or len(p2) > 50: raise ValueError("Palavra 2 do teste %d deve ter entre 1 e 50 caracteres" % teste_atual)

    if len(p1) > len(p2):
        maior = p1
        menor = p2
    else: 
        maior = p2
        menor = p1

    cursor_p1 = 0
    cursor_p2 = 0
    combinada = ""

    for idx in range(len(p1) + len(p2)):
        if idx % 2 == 0 and cursor_p1 < len(p1):
            combinada = combinada + p1[cursor_p1]
            cursor_p1 = cursor_p1 + 1
        elif cursor_p2 < len(p2):
            combinada = combinada + p2[cursor_p2]
            cursor_p2 = cursor_p2 + 1
        elif len(p1) > len(p2):
            combinada = combinada + p1[cursor_p1]
            cursor_p1 = cursor_p1 + 1
        else: 
            combinada = combinada + p2[cursor_p2]
            cursor_p2 = cursor_p2 + 1
    
    print(combinada)

for t in testes:
    teste(t[0], t[1])