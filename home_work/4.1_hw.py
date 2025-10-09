class Car:
    def __init__(self, text, color=None, type1=None, year=None):
        self.text: str = text
        self.color: str = color
        self.type1: str = type1
        self.year: int = year

    def start(self):
        return 'Автомобиль заведён'

    def stop(self):
        return 'Автомобиль заглушен'

    def set_year(self, x):
        self.year = x 
    
    def set_type(self, y):
        self.type1 = y

    def set_color(self, z):
        self.color = z


toyota = Car('Toyota')
toyota.set_year(2001)
toyota.set_type('Sedan')
toyota.set_color('Black')
print(toyota.text, toyota.color, toyota.type1, toyota.year)