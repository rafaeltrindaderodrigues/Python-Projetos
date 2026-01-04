"""

CONSTANTE = "Variáveis" que não vão mudar

Muitas condições no mesmo if (ruim)

    <- Contagem de complexidade (ruim)

"""

velocidade = 61  # velocidade atual do carro

local_carro = 105  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1

LOCAL_1 = 100  # local onde o radar 1 está

RADAR_RANGE = 1  # A distância onde o radar pega

# PASSO 1: VERIFICAR SE ELE ESTÁ DENTRO DO LIMITE DO RADAR
if (LOCAL_1 - RADAR_RANGE <= local_carro) and (local_carro <= LOCAL_1 + RADAR_RANGE):
    
    # Identificamos se ele está dentro do limite do radar, agora vamos para o próximo passo
    # PASSO 2: VERIFICAR SE O LIMITE DE VELOCIDADE ULTRAPASSOU O REQUERIDO PELA VIA
    if velocidade > RADAR_1:
        # criando uma variável para mutar por 80 reais acima de cada Km
        multa = (velocidade - RADAR_1) * 80
        print(f'Você está acima da velocidade. Terá que pagar uma multa de R${multa}\n')
        print(f'Dirija mais devagar e consciente!')

    # Avaliando a situação em que ele não está acima da velocidade:
    else:
        print('Você não está acima da velocidade.')
        print(f'{velocidade}Km de {RADAR_1}Km')

# PASSO 3: CRIANDO CONDIÇÕES DE ENTRAR NO RADAR E SAIR DO RADAR
# Entrada no radar
elif local_carro < LOCAL_1 - RADAR_RANGE:
    print(f'Você ainda não entrou no radar, faltam {(LOCAL_1 - RADAR_RANGE) - local_carro}Km')

# Saida do radar
elif local_carro > LOCAL_1 + RADAR_RANGE:   
    print(f'Você já passou pelo radar. Está {local_carro - (LOCAL_1 + RADAR_RANGE)}Km à frente') 






