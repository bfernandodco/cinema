from model.Cinema import Cinema


class Filme(Cinema):

    def __int__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self,nova_duracao):
        self._duracao = nova_duracao

    def imprime(self):
        return print(f'nome do filme: {self.nome} - ano: {self.ano}'
                     f' - duracao: {self.duracao}min - likes: {self.likes}')