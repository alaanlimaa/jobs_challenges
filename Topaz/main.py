from usuario import Usuario
from servidor import Servidor
from bcarga import BalancoDeCarga

with open('input.txt', 'r') as leitura, open('output.txt', 'w') as escreve:
    balanco_carga = BalancoDeCarga(leitura, escreve)
    Usuario.ttask = int(leitura.readline())
    Servidor.umax = int(leitura.readline())
    balanco_carga.executa_balanco()

