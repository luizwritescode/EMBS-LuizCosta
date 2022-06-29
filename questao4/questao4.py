#assumindo que a velocidade do invasor e 1 unidade por segundo

import math


linhas = []
while True:
    try: linha = input()
    except EOFError:
        break
    linhas.append(linha)

for linha in linhas:
    valores = [ int(x) for x in linha.split() ]
    fiddle_x, fiddle_y, inv_x, inv_y, inv_vel, raio_ultimate, raio_corvos = valores

    def fuga_invasor(inv_x, inv_y, inv_vel):
        if inv_vel == 0:
            return inv_x, inv_y

    def salto_fiddle(fiddle_x,fiddle_y, inv_x, inv_y, raio_ultimate):
        delta_x = inv_x - fiddle_x
        delta_y = inv_y - fiddle_y
        angulo = math.atan2(delta_y, delta_x) * 180 / math.pi

        new_fiddle_x = fiddle_x + math.cos(angulo) * raio_ultimate
        new_fiddle_y = fiddle_y + math.sin(angulo) * raio_ultimate

        return new_fiddle_x, new_fiddle_y
    
    def dentro_do_alcance(fiddle_x, fiddle_y, inv_x, inv_y, raio_corvos):
        pass

    new_inv_x, new_inv_y = fuga_invasor(inv_x, inv_y, inv_vel)
    new_fiddle_x, new_fiddle_y = salto_fiddle(fiddle_x, fiddle_y, new_inv_x,new_inv_y,raio_ultimate)

    print(new_inv_x, new_inv_y, new_fiddle_x,new_fiddle_y)
