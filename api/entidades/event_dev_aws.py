class EventDevAws():

    def __init__(self, name, place_name, distance, last_seen, utcdate):
        self.__name = name
        self.__place_name = place_name
        self.__distance = distance
        self.__last_seen = last_seen
        self.__utcdate = utcdate


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def place_name(self):
        return self.__place_name
    @place_name.setter
    def place_name(self, place_name):
        self.__place_name = place_name

    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self, distance):
        self.__distance = distance

    @property
    def last_seen(self):
        return self.__last_seen
    @last_seen.setter
    def last_seen(self, last_seen):
        self.__last_seen = last_seen

    @property
    def utcdate(self):
        return self.__utcdate
    @utcdate.setter
    def utcdate(self, utcdate):
        self.__utcdate = utcdate