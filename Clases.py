class DivisionByZeroError(Exception):

    def __init__(self, message: str):
        super(Exception, self).__init__(message)


Exception
