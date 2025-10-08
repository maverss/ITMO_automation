'''
class Button:

type: str = 'Кнопка'

    def __init__(self, text, link):
        self.text = text
        self.link = link

home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка '+ catalog_msk.text + ' имеет ссылка ' + catalog_msk.link)

class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc
    
    def click(self):
        return "Клик по локатору - {}".format(self.loc)


home_two = ButtonTwo('Домой', '/home', 'button#home')

print(home_two.click())

class input:
    def __init__(self, Loc):
        self.Loc = Loc

search = input('input#search')

print(search.Loc)

class input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = input('input#search', '12345')

print(search.loc, search.text)

class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

one = Button('Button#one', 'first')
two = Title('title#two', 'second')
three = Link('Link#three', 'third')

print(one.loc, one.text)
print(two.loc, two.text)
print(three.loc, three.text)


class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
        return "{}".format(self.url)

home = Page('/home')

print(home.get())
'''

class Soda:
    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        if self.add:
            print(self.add)
        else:
            print('Nothing')

cola = Soda('coke')
sprite = Soda()

print(cola.show_my_drink())
print(sprite.show_my_drink())