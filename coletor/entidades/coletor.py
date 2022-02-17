class Coletor():

    def __init__(self, address, place_id, place_name, battery, temperature, utcdate, connector_utcdate):
        self.__address = address
        self.__place_id = place_id
        self.__place_name = place_name
        self.__battery = battery
        self.__temperature = temperature
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
    def battery(self):
        return self.__battery
    @battery.setter
    def battery(self, battery):
        self.__battery = battery

    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature

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