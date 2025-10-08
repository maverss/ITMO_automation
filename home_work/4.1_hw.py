class Car:
    def __init__(self, text, color=None, type1=None, year=None):
        self.text: str = text
        self.color: str = color
        self.type1: str = type1
        self.year: int = year

    def Start(self):
        return 'Автомобиль заведён'

    def Stop(self):
        return 'Автомобиль заглушен'

    def Year(self, x):
        self.year = x 
    
    def Type(self, y):
        self.type1 = y

    def Color(self, z):
        self.color = z

Toyota = Car('Toyota')
Toyota.Year(2001)
Toyota.Type('Sedan')
Toyota.Color('Black')
print(Toyota.text, Toyota.color, Toyota.type1, Toyota.year)

