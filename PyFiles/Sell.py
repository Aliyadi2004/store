# Form implementation generated from reading ui file 'Sell.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_sellpage(object):
    def setupUi(self, sellpage):
        sellpage.setObjectName("sellpage")
        sellpage.resize(845, 570)
        sellpage.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=sellpage)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, -50, 960, 681))
        self.listView.setObjectName("listView")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 20, 670, 360))
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.Scout = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Scout.setGeometry(QtCore.QRect(350, 410, 160, 30))
        self.Scout.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Scout.setObjectName("Scout")
        self.SProCode = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.SProCode.setGeometry(QtCore.QRect(130, 410, 160, 30))
        self.SProCode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SProCode.setObjectName("SProCode")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 380, 90, 30))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 380, 90, 30))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.SellAddPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SellAddPB.setGeometry(QtCore.QRect(590, 410, 110, 30))
        self.SellAddPB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SellAddPB.setObjectName("SellAddPB")
        self.SellBackPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SellBackPB.setGeometry(QtCore.QRect(0, 0, 75, 24))
        self.SellBackPB.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.SellBackPB.setObjectName("SellBackPB")
        self.hiddenValue = QtWidgets.QLabel(parent=self.centralwidget)
        self.hiddenValue.setGeometry(QtCore.QRect(280, 100, 140, 110))
        self.hiddenValue.setObjectName("hiddenValue")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, -10, 190, 30))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.End = QtWidgets.QPushButton(parent=self.centralwidget)
        self.End.setGeometry(QtCore.QRect(370, 470, 70, 30))
        self.End.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.End.setObjectName("End")
        self.hiddenValue.raise_()
        self.listView.raise_()
        self.tableWidget.raise_()
        self.Scout.raise_()
        self.SProCode.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.SellBackPB.raise_()
        self.label_2.raise_()
        self.SellAddPB.raise_()
        self.End.raise_()
        sellpage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=sellpage)
        self.statusbar.setObjectName("statusbar")
        sellpage.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=sellpage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 22))
        self.menubar.setObjectName("menubar")
        sellpage.setMenuBar(self.menubar)

        self.retranslateUi(sellpage)
        QtCore.QMetaObject.connectSlotsByName(sellpage)

    def retranslateUi(self, sellpage):
        _translate = QtCore.QCoreApplication.translate
        sellpage.setWindowTitle(_translate("sellpage", "MainWindow"))
        self.tableWidget.setWhatsThis(_translate("sellpage", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("sellpage", "کد کالا"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("sellpage", "نام کالا"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("sellpage", "قیمت"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("sellpage", "تعداد"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("sellpage", "جمع"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("sellpage", "حذف "))
        self.label.setText(_translate("sellpage", "تعداد"))
        self.label_3.setText(_translate("sellpage", "نام کالا"))
        self.SellAddPB.setText(_translate("sellpage", "اضافه کردن"))
        self.SellBackPB.setText(_translate("sellpage", "بازگشت"))
        self.hiddenValue.setText(_translate("sellpage", "TextLabel"))
        self.label_2.setText(_translate("sellpage", "صفحه فروش"))
        self.End.setText(_translate("sellpage", "اتمام"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sellpage = QtWidgets.QMainWindow()
    ui = Ui_sellpage()
    ui.setupUi(sellpage)
    sellpage.show()
    sys.exit(app.exec())
