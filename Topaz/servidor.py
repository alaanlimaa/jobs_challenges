from usuario import Usuario
from excecoes import LimiteTtaskOrUmax


class Servidor:
    umax = 0

    def __init__(self, usuarios):
        self.usuarios = usuarios

    @staticmethod
    def verifica_limite_umax():
        if Servidor.umax < 1 or Servidor.umax > 10:
            raise LimiteTtaskOrUmax('UMAX tem que ser maior ou igual a 1 e menor ou igual a 10!')
        return 0

    def disponibilidade_servidor(self):
        """Verifica se o respectivo servidor tem disponibilidade para
        alocar mais usuários ou não, realiza a leitura da quantidade de
        usuários ativos no servidor e depois informa o status True = Disp.
        e False = indisp."""
        if len(self.usuarios) < Servidor.umax:
            return True
        else:
            return False

    def add_usuario(self):
        """Adiciona um usuário sem o mesmo estar dentro de uma lista"""
        self.usuarios.append(Usuario())

    def remove_tick_usuario(self):
        """Remove um tick de cada usuário que esteja conectado ao
         servidor, essa função é realizada a cada rodada de leitura do input.txt """

        self.usuarios[:] = [user for user in self.usuarios if user.remove_tick()]
        return self.usuarios






