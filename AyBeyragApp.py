import sys
from PyQt6 import QtWidgets
from PyFiles.mainpage import *
from PyFiles.CPR import *
from PyFiles.CG import *
from PyFiles.Sell import *
from Addings.CprAdd import *
from Addings.CgAdd import *
from Addings.Anbar import *
from PyFiles.Anbar import *
from sales.sale import *


def switchWindows(mainWin, mainWin2, runable = None):
    mainWin.hide()
    if runable is not None :
        runable() 
    mainWin2.show()

app = QtWidgets.QApplication(sys.argv)

mainpage = QtWidgets.QMainWindow()
mainUI = Ui_MainWindow()


Anberpage = QtWidgets.QMainWindow()
AnbarUI = Ui_AnbarPage()
AnbarUI.setupUi(Anberpage)


Selpage = QtWidgets.QMainWindow()
SellUI = Ui_sellpage()
SellUI.setupUi(Selpage)

Cgpage = QtWidgets.QMainWindow()
CgUI = Ui_CGpage()
CgUI.setupUi(Cgpage)


CPRpage = QtWidgets.QMainWindow()
CprUI = Ui_CPRpage()

mainUI.setupUi(mainpage)
mainpage.show()

CprUI.setupUi(CPRpage)

AnbarAddOj = AnbarAddcls(AnbarUI)

CprAddObj =CprAdd(CprUI)
CgAddObj = CgAddcls(CgUI)


SalesAddOj = SalesCls(SellUI)

# Anbaroj =

mainUI.CprPB.clicked.connect(lambda:switchWindows(mainpage,CPRpage,lambda:CprAddObj.rendercpr()))

mainUI.CgPB.clicked.connect(lambda:switchWindows(mainpage,Cgpage,lambda:CgAddObj.rendercg()))


mainUI.StorePB.clicked.connect(lambda:switchWindows(mainpage,Anberpage,lambda:AnbarAddOj.renderAnbar()))
AnbarUI.AnbarbackPB.clicked.connect(lambda:switchWindows(Anberpage,mainpage))
#


mainUI.SalePB.clicked.connect(lambda:switchWindows(mainpage,Selpage,lambda:SalesAddOj.renderSales()))
SellUI.SellAddPB.clicked.connect(lambda:SalesAddOj.SaleAdd())
SellUI.SellBackPB.clicked.connect(lambda:switchWindows(Selpage,mainpage))

SellUI.End.clicked.connect(lambda:SalesAddOj.Endfunc())



AnbarUI.AnbarAddPB.clicked.connect(lambda:AnbarAddOj.addusers())

CgUI.CgAddPB.clicked.connect(lambda:CgAddObj.addStd())

CgUI.CgBackPB.clicked.connect(lambda:switchWindows(Cgpage,mainpage))

CprUI.backPB.clicked.connect(lambda:switchWindows(CPRpage,mainpage))

CprUI.AddPB.clicked.connect(lambda:CprAddObj.addStd())

# 43785




sys.exit(app.exec())
