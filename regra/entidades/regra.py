class Regra():

    def __init__(self, name, description, tempPermanencia, plan, mio, event, action, portout, portin, state):
        self.__name = name
        self.__description = description
        self.__tempPermanencia = tempPermanencia
        self.__plan = plan
        self.__mio = mio
        self.__event = event
        self.__action = action
        self.__portout = portout
        self.__portin = portin
        self.__state = state

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
    def tempPermanencia(self):
        return self.__tempPermanencia
    @tempPermanencia.setter
    def tempPermanencia(self, tempPermanencia):
        self.__tempPermanencia = tempPermanencia

    @property
    def plan(self):
        return self.__plan
    @plan.setter
    def plan(self, plan):
        self.__plan = plan

    @property
    def mio(self):
        return self.__mio
    @mio.setter
    def plan(self, mio):
        self.__mio = mio

    @property
    def event(self):
        return self.__event
    @event.setter
    def event(self, event):
        self.__event = event

    @property
    def action(self):
        return self.__action
    @action.setter
    def action(self, action):
        self.__action = action

    @property
    def portout(self):
        return self.__portout
    @portout.setter
    def portout(self, portout):
        self.__portout = portout

    @property
    def portin(self):
        return self.__portin
    @portin.setter
    def portin(self, portin):
        self.__portin = portin

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state