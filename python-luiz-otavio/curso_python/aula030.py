"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 660 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_pass_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
      local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_pass_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Passou da velocidade máxima')

if carro_pass_radar_1:
    print('Passou no radar')

if carro_multado_radar_1:
    print('Carro multado em RADAR 1')