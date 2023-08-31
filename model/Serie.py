from model.Cinema import Cinema


class Serie(Cinema):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def duracao(self):
        return self._temporadas

    @temporadas.setter
    def temporadas(self, nova_temporada):
        self._temporadas = nova_temporada

    def imprime(self):
        return print(f'nome da série: {self.nome} - ano: {self.ano}'
                     f' - temporadas: {self.temporadas} - likes: {self.likes}')