"""
Описать абстрактный класс Device:

- определить абстрактный метод process_doc, который принимает аргумент name -
  название документа и будет бросать raise NotImplementedError

Описать класс Scanner, который наследуется от Device:

- переопределить метод process_doc, который будет возвращать строку
  "Сканирую документ: {name}"

Описать класс Copier, который наследуется от Device:

- переопределить метод process_doc, который будет возвращать строку
  "Делаю копию: {name}"

Описать класс MFU, который наследуется от Scanner и Copier:

- переопределить метод process_doc, который будет возвращать строку
  "Сканирую, отправляю факс: {name}"

В блоке if "__name__" == "__main__": создать объект класса MFU. Просмотреть MRO
"""

class Device:
    def process_doc(self, name):
        raise NotImplementedError

class Scanner(Device):
    def process_doc(self, name):
        return f"Сканирую документ: {name}"

class Copier(Device):
    def process_doc(self, name):
        return f"Делаю копию: {name}"

class MFU(Scanner, Copier):
    def process_doc(self, name):
        return f"Сканирую, отправляю факс: {name}"

if __name__ == '__main__':
    mfu = MFU()