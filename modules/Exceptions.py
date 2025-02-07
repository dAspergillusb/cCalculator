

class WrongLanguageInConfig(Exception):
    """
    Exception raised when in main config file var language is wrong
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

