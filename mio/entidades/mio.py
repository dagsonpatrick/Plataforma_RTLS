class Mio():

    def __init__(self, name, description, ip, port, qtdInputs, qtdOutputs, hostListener, portListener):

        self.__name = name
        self.__description = description
        self.__ip = ip
        self.__port = port
        self.__qtdInputs = qtdInputs
        self.__qtdOutputs = qtdOutputs
        self.__hostListener = hostListener
        self.__portListener = portListener

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
    def ip(self):
        return self.__ip
    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    @property
    def port(self):
        return self.__port
    @port.setter
    def port(self, port):
        self.__port = port

    @property
    def qtdInputs(self):
        return self.__qtdInputs
    @qtdInputs.setter
    def qtdInputs(self, qtdInputs):
        self.__qtdInputs = qtdInputs

    @property
    def qtdOutputs(self):
        return self.__qtdOutputs
    @qtdOutputs.setter
    def qtdInputs(self, qtdOutputs):
        self.__qtdOutputs = qtdOutputs

    @property
    def hostListener(self):
        return self.__hostListener
    @hostListener.setter
    def hostListener(self, hostListener):
        self.__hostListener = hostListener

    @property
    def portListener(self):
        return self.__portListener
    @portListener.setter
    def portListener(self, portListener):
        self.__portListener = portListener