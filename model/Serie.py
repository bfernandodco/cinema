from model.Cinema import Cinema


class Serie(Cinema):

    def __int__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def duracao(self):
        return self._temporadas

    @duracao.setter
    def duracao(self, nova_temporadas):
        self._temporadas = nova_temporadas

    def imprime(self):
        return print(f'nome da serie: {self.nome} - ano: {self.ano}'
                     f' - temporadas: {self.temporadas}min - likes: {self.likes}')