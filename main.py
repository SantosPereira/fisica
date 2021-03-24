def força_gravitacional():
    g = 6.674184 * 10**-11 #constante gravitacional
    d = float(input('Distância entre os corpos: ')) #metros #distancia entre os corpos

    corpo1 = int(input('Massa do corpo 1: ')) #quilograma #massa
    corpo2 = int(input('Masaa do corpo 2: ')) #massa

    tempo = int(input('Escala temporal: ')) # múltiplo de 10 #tempo por ciclo while #segundos
    cont_tempo = 0

    while True:
        f = g * ((corpo1 * corpo2)/d**2)
        if d <= 0:
            break
        else:
            d = d - (tempo*f)
        cont_tempo += 1
        print(d)

    corr_tempo = cont_tempo*tempo #correção da temporal # o último número é igual a quantidade de zeros na variavel "tempo" + 1

    print(f'Tempo total até objetos colidirem {corr_tempo} segundos, ou {(corr_tempo)/60} minutos, ou {(corr_tempo)/60/60} horas,\n ou {(corr_tempo)/60/60/24} dias, ou {(corr_tempo)/60/60/24/365} anos, ou {(corr_tempo)/60/60/24/365/100} séculos, ou {(corr_tempo)/60/60/24/365/1000} milênios')
    print(f'Velocidade {d/corr_tempo} m/s, ou {d/corr_tempo*3.6} km/h')

força_gravitacional()
