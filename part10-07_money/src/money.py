# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents
    
    def __lt__(self, another):
        return (self.__euros, self.__cents) < (another.__euros, another.__cents)

    def __gt__(self, another):
        return (self.__euros, self.__cents) > (another.__euros, another.__cents)

    def __add__(self, another):
        total_cents = self.__cents + another.__cents
        total_euros = self.__euros + another.__euros + total_cents // 100
        total_cents = total_cents % 100
        return Money(total_euros, total_cents)

    def __sub__(self, another):
        total_cents_self = self.__euros * 100 + self.__cents
        total_cents_another = another.__euros * 100 + another.__cents
        total_cents = total_cents_self - total_cents_another
        if total_cents < 0:
            raise ValueError("a negative result is not allowed")
        total_euros = total_cents // 100
        total_cents = total_cents % 100
        return Money(total_euros, total_cents)