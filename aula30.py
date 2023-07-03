velocidade = 61
local_carro = 100

# Constantes
RADAR_1 = 60  # Velocidade máxima permitida
LOCAL_RADAR_1 = 100  # Local onde o radar 1 está
RADAR_RANGE = 1

range_max_radar_1 = LOCAL_RADAR_1 + RADAR_RANGE
range_min_radar_1 = LOCAL_RADAR_1 - RADAR_RANGE
vel_excedida_radar_1 = velocidade > RADAR_1
carro_range_max_radar_1 = local_carro <= range_max_radar_1
carro_range_min_radar_1 = local_carro >= range_min_radar_1

carro_dentro_radar_1 = carro_range_max_radar_1 and \
    carro_range_min_radar_1

carro_multado = carro_dentro_radar_1 and vel_excedida_radar_1

if carro_dentro_radar_1:
    print('Carro passou no radar 1')
if vel_excedida_radar_1:
    print('Velocidade acima do radar 1')
if carro_multado:
    print('Carro multado no radar 1')





