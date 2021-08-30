from excecoes import LimiteTtaskOrUmax, MenorQueZeroTtask


class Usuario:
    ttask = 0

    def __init__(self, ):
        self.ttask = Usuario.ttask

    @staticmethod
    def verifica_limite_ttask():
        if Usuario.ttask < 1 or Usuario.ttask > 10:
            raise LimiteTtaskOrUmax('TTASK tem que ser maior ou igual a 1 e menor ou igual a 10!')
        return 0

    def remove_tick(self):
        """Remove um tick do ttask"""
        self.ttask -= 1
        if self.ttask < 0:
            raise MenorQueZeroTtask('TTASK não pode ter o seu respectivo valor menor que ZERO')
        return self.ttask

