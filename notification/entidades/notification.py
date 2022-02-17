class Notification():

    def __init__(self, description, timestamp_notification, collaborator, plano,  tag, usuario_check):
        self.__description = description
        self.__timestamp_notification= timestamp_notification
        self.__collaborator = collaborator
        self.__plano =  plano
        self.__tag = tag
        self.__usuario_check = usuario_check

@property
def description(self):
    return self.__description
@description.setter
def description(self, description):
    self.__description = description

@property
def timestamp_notification(self):
    return self.__timestamp_notification
@timestamp_notification.setter
def timestamp_notification(self, timestamp_notification):
    self.__timestamp_notification = timestamp_notification