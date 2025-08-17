import re
import sys # Только для доступа к аргументам командной строки
from pprint import pprint

from PySide6.QtWidgets import QApplication, QMainWindow

from qt import MainUi
page_source = ''

with open("page_source.html") as f:
    page_source = f.read()

ads = re.findall("\/kaliningrad\/.+?(?=\")", page_source)

ads = list(set(ads))
data = list()
for ad in ads:
    city, cat = ad.split("/")[1], ad.split("/")[2]
    data.append([city, cat, "https://www.avito.ru/" + ad])
pprint(data)
print(f"\n\n\n\t---\t{len(ads)}\t---")

# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
app = QApplication(sys.argv)

# Создаём виджет Qt — окно.
window = QMainWindow()
mainUi = MainUi()
mainUi.setupUi(window)
mainUi.updateItems(data)
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()


# Приложение не доберётся сюда, пока вы не выйдете и цикл
# событий не остановится.


