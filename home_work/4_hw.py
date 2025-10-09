class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def s(self):
        return self.height * self.width

    def p(self):
        return 2 * self.height + 2 * self.width


r1 = Rectangle(2, 2)
r2 = Rectangle(3, 3)
r3 = Rectangle(4, 4)

print(r1.p(), r2.p(), r3.p(), r1.s(), r2.s(), r3.s())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


math1 = Math(10, 5)
print(math1.addition(), math1.multiplication(), math1.division(), math1.subtraction())


class Button:
    type: str = "Кнопка"

    def __init__(self, text, loc=None):
        self.text = text
        self.loc = loc
    
    def click(self):
        return "Клик по кнопке '{}'".format(self.text)


text_box = Button('Text Box')
check_box = Button('Check Box')
radio_button = Button('Radio Button')
web_tables = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
broken_links_images = Button('Broken Links - Images')
upload_and_download = Button('Upload and Download')
dynamic_properties = Button('Dynamic Properties')
practice_form = Button('Practice Form')
browser_windows = Button('Browser Windows')
alerts = Button('Alerts')
frames = Button('Frames')
nested_frames = Button('Nested Frames')
modal_dialogs = Button('Modal Dialogs')
accordian = Button('Accordian')
auto_complete = Button('Auto Complete')
date_picker = Button('Date Picker')
slider = Button('Slider')
progress_bar = Button('Progress Bar')
tabs = Button('Tabs')
tool_tips = Button('Tool Tips')
menu = Button('Menu')
select_menu = Button('Select Menu')
sortable = Button('Sortable')
selectable = Button('Selectable')
resizable = Button('Resizable')
droppable = Button('Droppable')
dragabble = Button('Dragabble')
login = Button('Login')
book_store = Button('Book Store')
profile = Button('Profile')
book_store_api = Button('Book Store API')

print(text_box.text, "-", text_box.click())
print(check_box.text, "-", check_box.click())
print(radio_button.text, "-", radio_button.click())
print(web_tables.text, "-", web_tables.click())
print(buttons.text, "-", buttons.click())
print(links.text, "-", links.click())
print(broken_links_images.text, "-", broken_links_images.click())
print(upload_and_download.text, "-", upload_and_download.click())
print(dynamic_properties.text, "-", dynamic_properties.click())
print(practice_form.text, "-", practice_form.click())
print(browser_windows.text, "-", browser_windows.click())
print(alerts.text, "-", alerts.click())
print(frames.text, "-", frames.click())
print(nested_frames.text, "-", nested_frames.click())
print(modal_dialogs.text, "-", modal_dialogs.click())
print(accordian.text, "-", accordian.click())
print(auto_complete.text, "-", auto_complete.click())
print(date_picker.text, "-", date_picker.click())
print(slider.text, "-", slider.click())
print(progress_bar.text, "-", progress_bar.click())
print(tabs.text, "-", tabs.click())
print(tool_tips.text, "-", tool_tips.click())
print(menu.text, "-", menu.click())
print(select_menu.text, "-", select_menu.click())
print(sortable.text, "-", sortable.click())
print(selectable.text, "-", selectable.click())
print(resizable.text, "-", resizable.click())
print(droppable.text, "-", droppable.click())
print(dragabble.text, "-", dragabble.click())
print(login.text, "-", login.click())
print(book_store.text, "-", book_store.click())
print(profile.text, "-", profile.click())
print(book_store_api.text, "-", book_store_api.click())