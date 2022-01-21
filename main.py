from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import uic
import sqlite3


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.tableWidget.setColumnWidth(0, 120)  # pеализация таблицы
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.setColumnWidth(3, 130)
        self.tableWidget.setColumnWidth(4, 130)
        self.tableWidget.setColumnWidth(5, 130)
        self.tableWidget.setColumnWidth(6, 130)
        self.tableWidget.setColumnWidth(7, 130)
        self.tableWidget.setHorizontalHeaderLabels(["id", "title", "degree", "sort", 'description', 'price', 'volume'])
        self.loaddata()  # выводит значение таблицы

    def loaddata(self):  # обновляет значения таблицы
        connection = sqlite3.connect('coffee.sqlite')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM rrr LIMIT 15'

        tablerow = 0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(15)
        for row in results:
            print(row)
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            tablerow += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())