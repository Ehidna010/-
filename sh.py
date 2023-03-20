class discs:
    def __init__(self, text, image):
        self.text = text
        self.image = image

class sh:
    def __init__(self, theme: type.__str__, discription: type.__str__, images):
        self.theme = theme
        self.discription = discription
        self.images = images
        self.iter = 0

    def nextImage(self):
        self.iter += 1
        if self.iter < len(self.images):
            return self.images[iter]
        return 0

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

array = list[sh]

class Callback:
    def __init__(self, message, kb, image):
        self.message = message
        self.image = image
        self.kb = kb

class shController:
    def __init__(self, shs: array):
        self.shs = shs
        self.sh = None

    def getStartMenu(self):
        menu = ReplyKeyboardMarkup()
        for i in self.shs:
            menu.add(KeyboardButton(i.theme))

        return menu

    def getSh(self, theme):
        for i in self.shs:
            if i.theme == theme:
                sh = i
                break
        
        kb = ReplyKeyboardMarkup()

        if theme == 'Закрыть':
            sh = None
            return Callback('Главное меню', self.getStartMenu(), None)

        kb.add(KeyboardButton('Закрыть'))

        if theme == 'Не понял тему':
            ni = sh.nextImage()
        else:
            ni = sh.images[sh.iter]

        if sh == None:
            return Callback('Такой темы нет', kb, None)

        if len(sh.images) > 0 and ni != 0:
            kb.row(KeyboardButton('Не понял тему'))
            

        return Callback(sh.theme + ':\n\n' + sh.discription, kb, ni)