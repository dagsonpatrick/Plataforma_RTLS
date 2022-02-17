class User():
    def __init__(self, username, first_name, last_name, email, password):
        self.__username = username
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.password = password