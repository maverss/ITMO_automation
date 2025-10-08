class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def S(self):
        return self.height * self.width

    def P(self):
        return 2 * self.height + 2 * self.width

r1 = rectangle(2, 2)
r2 = rectangle(3, 3)
r3 = rectangle(4, 4)

print(r1.P(), r2.P(), r3.P(), r1.S(), r2.S(), r3.S())

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

Math1 = Math(10, 5)
print(Math1.addition(), Math1.multiplication(), Math1.division(), Math1.subtraction())

class Button:
    type: str = "Кнопка"

    def __init__(self, text, loc=None):
        self.text = text
        self.loc = loc
    
    def click(self):
        return "Клик по кнопке '{}'".format(self.text)

TextBox = Button('Text Box')
CheckBox = Button('Check Box')
RadioButton = Button('Radio Button')
WebTables = Button('Web Tables')
Buttons = Button('Buttons')
Links = Button('Links')
BrokenLinksImages = Button('Broken Links - Images')
UploadAndDownload = Button('Upload and Download')
DynamicProperties = Button('Dynamic Properties')
PracticeForm = Button('Practice Form')
BrowserWindows = Button('Browser Windows')
Alerts = Button('Alerts')
Frames = Button('Frames')
NestedFrames = Button('Nested Frames')
ModalDialogs = Button('Modal Dialogs')
Accordian = Button('Accordian')
AutoComplete = Button('Auto Complete')
DatePicker = Button('Date Picker')
Slider = Button('Slider')
ProgressBar = Button('Progress Bar')
Tabs = Button('Tabs')
ToolTips = Button('Tool Tips')
Menu = Button('Menu')
SelectMenu = Button('Select Menu')
Sortable = Button('Sortable')
Selectable = Button('Selectable')
Resizable = Button('Resizable')
Droppable = Button('Droppable')
Dragabble = Button('Dragabble')
Login = Button('Login')
BookStore = Button('Book Store')
Profile = Button('Profile')
BookStoreAPI = Button('Book Store API')

print(TextBox.text, "-", TextBox.click())
print(CheckBox.text, "-", CheckBox.click())
print(RadioButton.text, "-", RadioButton.click())
print(WebTables.text, "-", WebTables.click())
print(Buttons.text, "-", Buttons.click())
print(Links.text, "-", Links.click())
print(BrokenLinksImages.text, "-", BrokenLinksImages.click())
print(UploadAndDownload.text, "-", UploadAndDownload.click())
print(DynamicProperties.text, "-", DynamicProperties.click())
print(PracticeForm.text, "-", PracticeForm.click())
print(BrowserWindows.text, "-", BrowserWindows.click())
print(Alerts.text, "-", Alerts.click())
print(Frames.text, "-", Frames.click())
print(NestedFrames.text, "-", NestedFrames.click())
print(ModalDialogs.text, "-", ModalDialogs.click())
print(Accordian.text, "-", Accordian.click())
print(AutoComplete.text, "-", AutoComplete.click())
print(DatePicker.text, "-", DatePicker.click())
print(Slider.text, "-", Slider.click())
print(ProgressBar.text, "-", ProgressBar.click())
print(Tabs.text, "-", Tabs.click())
print(ToolTips.text, "-", ToolTips.click())
print(Menu.text, "-", Menu.click())
print(SelectMenu.text, "-", SelectMenu.click())
print(Sortable.text, "-", Sortable.click())
print(Selectable.text, "-", Selectable.click())
print(Resizable.text, "-", Resizable.click())
print(Droppable.text, "-", Droppable.click())
print(Dragabble.text, "-", Dragabble.click())
print(Login.text, "-", Login.click())
print(BookStore.text, "-", BookStore.click())
print(Profile.text, "-", Profile.click())
print(BookStoreAPI.text, "-", BookStoreAPI.click())