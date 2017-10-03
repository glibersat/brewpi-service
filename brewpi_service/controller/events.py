from circuits import Event


class ControllerConnected(Event):
    """
    When a controller connects
    """
    def __init__(self, aController):
        super(ControllerConnected, self).__init__()
        self.controller = aController


class ControllerDisconnected(Event):
    pass


class ControllerBlockList(Event):
    def __init__(self, aController, aBlockList):
        super(ControllerBlockList, self).__init__()
        self.controller = aController
        self.blocks = aBlockList


class ControllerRequestCurrentProfile(Event):
    pass
