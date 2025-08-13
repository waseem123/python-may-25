class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def isValidAge(age):
    if age < 18:
        raise InvalidAgeError(f'{age} is not a valid age')
    else:
        return True


age = int(input('ENTER YOUR AGE - '))
try:
    print(isValidAge(age))
except InvalidAgeError as e:
    print(e)
