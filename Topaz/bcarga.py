from usuario import Usuario
from servidor import Servidor


class BalancoDeCarga:

    def __init__(self, leitura, escrita):
        self.input_txt = leitura
        self.output_txt = escrita
        self.servidores = []
        self.users_ativos = 0
        self.valor_custo_servidor = 0

    def cria_servidor(self):
        self.servidores.append(Servidor([Usuario()]))

    def aloca_usuarios(self, qtd_usuarios):
        for user in range(qtd_usuarios):
            foi_alocado = False
            for servidor in self.servidores:
                if servidor.disponibilidade_servidor():
                    servidor.add_usuario()
                    foi_alocado = True
            if not foi_alocado:
                self.cria_servidor()

    def ler_outro_tick(self):
        novos_users = self.input_txt.readline()
        if novos_users:
            return int(novos_users)
        else:
            return False

    def remove_tick_usuario_do_servidor(self):
        self.servidores[:] = [servidor for servidor in self.servidores if servidor.remove_tick_usuario()]

    def usuarios_ainda_ativos_no_servidor(self):
        cont = 0
        for servidor in self.servidores:
            cont += len(servidor.usuarios)
        return cont

    def escreve_resultado_final(self):
        self.output_txt.write(str(f'{self.usuarios_ainda_ativos_no_servidor()}\n' ))
        self.output_txt.write(str(self.valor_custo_servidor))

    def escreve_saida_cada_tick(self):
        saida = ''
        for num, servidor in enumerate(self.servidores):
            if num + 1 == len(self.servidores):
                saida += f'{len(servidor.usuarios)}\n'
            else:
                saida += f'{len(servidor.usuarios)},'

        self.output_txt.write(saida)
        return saida

    def executa_balanco(self):
        leitura_input = False
        while self.servidores or not leitura_input:
            numero_novos_user = self.ler_outro_tick()

            if numero_novos_user is False and leitura_input is False:
                leitura_input = True
            if not leitura_input:
                self.aloca_usuarios(numero_novos_user)

            self.escreve_saida_cada_tick()
            self.valor_custo_servidor += len(self.servidores)
            self.remove_tick_usuario_do_servidor()

        self.escreve_resultado_final()





