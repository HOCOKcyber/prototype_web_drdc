from enum import Enum


# Приватный класс!??!?!
# Серьезно в python нет нормального ООП!??!?!
class RequestInfo():
    def __init__(self, categoryTitle, descriptionTitle  ):
        self.categoryTitle = categoryTitle
        self.descriptionTitle = descriptionTitle


# Используется в шаблоне "templateRequestPage" в качестве переменной info
# Страницы по сути одинаковые только слова меняются
class RequestTemplate(Enum):
    MAINTENANCE = RequestInfo("Категория заявки", "Описание требований к работе")
    INCIDENT = RequestInfo("Категория инцидента", "Описание инцидента")