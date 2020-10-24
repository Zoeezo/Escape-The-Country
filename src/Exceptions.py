class HpZeroError(Exception):
    '''Raised when HP goes to zero'''

    def __init__(self, message="HP is 0 or smaller!"):
        self.message = message
        super().__init__(self.message)