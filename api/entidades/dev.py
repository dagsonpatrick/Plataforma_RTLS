
class Dev():

    def __init__(self, address, place_id, place_name, utcdate, connector_utcdate):
        self.__address = address
        self.__place_id = place_id
        self.__place_name = place_name
        self.__utcdate = utcdate
        self.__connector_utcdate = connector_utcdate

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def place_id(self):
        return self.__place_id

    @place_id.setter
    def place_id(self, place_id):
        self.__place_id = place_id

    @property
    def place_name(self):
        return self.__place_name

    @place_name.setter
    def place_name(self, place_name):
        self.__place_name = place_name

    @property
    def utcdate(self):
        return self.__utcdate

    @utcdate.setter
    def utcdate(self, utcdate):
        self.__utcdate = utcdate

    @property
    def connector_utcdate(self):
        return self.__connector_utcdate

    @connector_utcdate.setter
    def connector_utcdate(self, connector_utcdate):
        self.__connector_utcdate = connector_utcdate