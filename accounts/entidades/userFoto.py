class UserFoto():

    def __init__(self, foto, usuario):
        self.__foto = foto
        self.__usuario = usuario

    @property
    def foto(self):
        return self.__foto
    @foto.setter
    def foto(self, foto):
        self.__foto = foto

    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario