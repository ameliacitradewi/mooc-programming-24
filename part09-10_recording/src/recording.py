# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length: int):
        self.__length = length
        if length < 0:
            raise ValueError("The amount must be bigger than zero")
    
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("The amount must be bigger than zero")

# # Example Usage
the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)