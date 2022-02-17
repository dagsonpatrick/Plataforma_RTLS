
class Anchor():

    def __init__(self, description, address):
        self.__description = description
        self.__address = address


    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description = description


    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address):
        self.__address = address


