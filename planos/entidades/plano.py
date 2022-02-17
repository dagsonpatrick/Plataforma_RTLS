
class Plano():

    def __init__(self, nome, descricao, tempPermanencia, foto):
        self.__nome = nome
        self.__descricao = descricao
        self.__tempPermanencia = tempPermanencia
        self.__foto = foto


    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def tempPermanencia(self):
        return self.__tempPermanencia
    @tempPermanencia.setter
    def tempPermanencia(self, tempPermanencia):
        self.__tempPermanencia = tempPermanencia


    @property
    def foto(self):
        return self.__foto
    @foto.setter
    def foto(self, foto):
        self.__foto = foto

