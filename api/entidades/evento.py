class Evento():

    def __init__(self, idanchor, idtag, idcolaborador, dtInicio, dtFim, permanencia, status):
        self.__idanchor = idanchor
        self.__idtag = idtag
        self.__idcolaborador = idcolaborador
        self.__dtInicio = dtInicio
        self.__dtFim = dtFim
        self.__permanencia = permanencia
        self.__status = status

    @property
    def idanchor(self):
        return self.__idanchor
    @idanchor.setter
    def idanchor(self,idanchor):
        self.__idanchor = idanchor

    @property
    def idtag(self):
        return self.__idtag
    @idtag.setter
    def idtag(self, idtag):
        self.__idtag = idtag

    @property
    def idcolaborador(self):
        return self.__idcolaborador
    @idcolaborador.setter
    def idcolaborador(self, idcolaborador):
        self.__idcolaborador = idcolaborador

    @property
    def dtInicio(self):
        return self.__dtInicio
    @dtInicio.setter
    def dtInicio(self, dtInicio):
        self.__dtInicio = dtInicio

    @property
    def dtFim(self):
        return self.__dtFim
    @dtFim.setter
    def dtFim(self, dtFim):
        self.__dtFim = dtFim

    @property
    def permanencia(self):
        return self.__permanencia
    @permanencia.setter
    def permanencia(self, permanencia):
        self.__permanencia = permanencia

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        self.__status = status