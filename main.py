g = 6.674184 * 10**-11 #constante gravitacional
d = 3 #metros #distancia entre os corpos

objeto1 = 75000 #quilograma #massa
objeto2 = 65 #massa

tempo = 100 #tempo por ciclo while #segundos
cont_tempo = 0

while True:
    f = g * ((objeto1 * objeto2)/d**2)
    if d <= 0:
        breakhsthgtjyhjsyjsk
    else:
        d = d - (tempo*f)
    cont_tempo += 1
    print(d)

corr_tempo = cont_tempo*10**3 #correção da temporal # o último número é igual a quantidade de zeros na variavel "tempo" + 1

print(f'Tempo total até objetos colidirem {corr_tempo} segundos, ou {(corr_tempo)/60} minutos, ou {(corr_tempo)/60/60} horas,\n ou {(corr_tempo)/60/60/24} dias, ou {(corr_tempo)/60/60/24/365} anos, ou {(corr_tempo)/60/60/24/365/100} séculos, ou {(corr_tempo)/60/60/24/365/1000} milênios')
print(f'Velocidade {d/corr_tempo} m/s, ou {d/corr_tempo*3.6} km/h')







nfdvifuyvfffffffffffffffffffffffghfgwuj