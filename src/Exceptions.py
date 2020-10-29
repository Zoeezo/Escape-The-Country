class moneyZeroError(Exception):
    '''Raised when money goes below zero'''

    def __init__(self, message='Money is lower than 0!'):
        self.message = message
        super().__init__(self.message)

class itemNonExistantError(Exception):
    '''Raised when player does not have item in inventory'''

    def __init__(self, message='That item does not exist in players inventory!'):
        self.message = message
        super().__init__(self.message)