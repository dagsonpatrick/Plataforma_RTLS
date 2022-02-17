class Ativo():

    def __init__(self, name, description, statusAssociacao):
        self.__name = name
        self.__description = description
        self.__statusAssociacao = statusAssociacao

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def statusAssociacao(self):
        return self.__statusAssociacao
    @statusAssociacao.setter
    def statusAssociacao(self, statusAssociacao):
        self.__statusAssociacao = statusAssociacao

