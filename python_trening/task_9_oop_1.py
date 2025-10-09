from task_9_checks import Checks


class ButtonTwo(Checks):
    def __init__(self, text, link, loc):
        super().__init__(loc)
        self.text = text
        self.link = link
    
    def click(self):
        return "Клик по локатору - {}".format(self.loc)


home_two = ButtonTwo('Домой', '/home', 'button#home')
print(home_two.click())


class Input(Checks):
    def __init__(self, loc):
        super().__init__(loc)


search = Input('input#search')
print(search.loc)


class InputWithText(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


search_with_text = InputWithText('input#search', '12345')
print(search_with_text.loc, search_with_text.text)


class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


one = Button('Button#one', 'first')
two = Title('title#two', 'second')
three = Link('Link#three', 'third')

print(one.loc, one.text)
print(two.loc, two.text)
print(three.loc, three.text)