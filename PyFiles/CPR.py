# Form implementation generated from reading ui file 'CPR.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CPRpage(object):
    def setupUi(self, CPRpage):
        CPRpage.setObjectName("CPRpage")
        CPRpage.resize(967, 570)
        CPRpage.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=CPRpage)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, -50, 980, 681))
        self.listView.setObjectName("listView")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 20, 780, 360))
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.NameKh = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.NameKh.setGeometry(QtCore.QRect(130, 410, 150, 30))
        self.NameKh.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NameKh.setObjectName("NameKh")
        self.Adres = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Adres.setGeometry(QtCore.QRect(450, 410, 150, 30))
        self.Adres.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Adres.setObjectName("Adres")
        self.shomareh = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.shomareh.setGeometry(QtCore.QRect(290, 410, 150, 30))
        self.shomareh.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.shomareh.setObjectName("shomareh")
        self.tarikh = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tarikh.setGeometry(QtCore.QRect(610, 410, 150, 30))
        self.tarikh.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tarikh.setObjectName("tarikh")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 380, 90, 30))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 380, 90, 30))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 380, 90, 30))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 380, 90, 30))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.AddPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AddPB.setGeometry(QtCore.QRect(410, 470, 110, 30))
        self.AddPB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AddPB.setObjectName("AddPB")
        self.EditPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.EditPB.setGeometry(QtCore.QRect(410, 470, 110, 30))
        self.EditPB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EditPB.setObjectName("EditPB")
        self.backPB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backPB.setGeometry(QtCore.QRect(0, 0, 60, 24))
        self.backPB.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.backPB.setObjectName("backPB")
        self.hiddenValue = QtWidgets.QLabel(parent=self.centralwidget)
        self.hiddenValue.setGeometry(QtCore.QRect(280, 100, 140, 110))
        self.hiddenValue.setObjectName("hiddenValue")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, -10, 190, 30))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.hiddenValue.raise_()
        self.listView.raise_()
        self.tableWidget.raise_()
        self.NameKh.raise_()
        self.Adres.raise_()
        self.shomareh.raise_()
        self.tarikh.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.backPB.raise_()
        self.label_2.raise_()
        self.EditPB.raise_()
        self.AddPB.raise_()
        CPRpage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=CPRpage)
        self.statusbar.setObjectName("statusbar")
        CPRpage.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=CPRpage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 22))
        self.menubar.setObjectName("menubar")
        CPRpage.setMenuBar(self.menubar)

        self.retranslateUi(CPRpage)
        QtCore.QMetaObject.connectSlotsByName(CPRpage)

    def retranslateUi(self, CPRpage):
        _translate = QtCore.QCoreApplication.translate
        CPRpage.setWindowTitle(_translate("CPRpage", "MainWindow"))
        self.tableWidget.setWhatsThis(_translate("CPRpage", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("CPRpage", "کد کاربر "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("CPRpage", "نام طرف خرید"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("CPRpage", "شماره موبایل"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("CPRpage", "ادرس"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("CPRpage", "تاریخ"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("CPRpage", "حذف"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("CPRpage", "ویرایش"))
        self.label.setText(_translate("CPRpage", "نام طرف خرید"))
        self.label_3.setText(_translate("CPRpage", "ادرس"))
        self.label_4.setText(_translate("CPRpage", "شماره موبایل"))
        self.label_5.setText(_translate("CPRpage", "تاریخ"))
        self.AddPB.setText(_translate("CPRpage", "اضافه کردن"))
        self.EditPB.setText(_translate("CPRpage", "ویرایش"))
        self.backPB.setText(_translate("CPRpage", "بازگشت"))
        self.hiddenValue.setText(_translate("CPRpage", "TextLabel"))
        self.label_2.setText(_translate("CPRpage", "اقای بیرق خدمتیز دع"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CPRpage = QtWidgets.QMainWindow()
    ui = Ui_CPRpage()
    ui.setupUi(CPRpage)
    CPRpage.show()
    sys.exit(app.exec())
