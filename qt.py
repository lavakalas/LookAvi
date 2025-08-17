from qt_creator import Ui_MainWindow

from PySide6.QtWidgets import QTableWidgetItem

class MainUi(Ui_MainWindow):
    def updateItems(self, items):
        self.tableWidget.setRowCount(len(items))
        self.tableWidget.setColumnWidth(2, 400)
        for i, (city, category, link) in enumerate(items):
            item_city = QTableWidgetItem(city)
            item_category = QTableWidgetItem(category)
            item_link = QTableWidgetItem(link)
            self.tableWidget.setItem(i, 0, item_city)
            self.tableWidget.setItem(i, 1, item_category)
            self.tableWidget.setItem(i, 2, item_link)
