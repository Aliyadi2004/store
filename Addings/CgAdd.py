from PyQt6 import QtWidgets
from Addings.Model import *
import secrets
#text = 'cvh'
#name = f'matn ma {text} ast'
#name1 = 'matn ma %s ast' %text
#print(text,'\n',name,'\n',name1)


class CgAddcls:
    def __init__(self, ui):
        self.ui = ui
        self.model = Model()
        
        

    def rendercg(self):
        self.ui.tableWidget.setRowCount(0)
        stdList = self.model.restore("select id, ProductID ,Product, BuyPrice, SelePrice from cg")

        for std in stdList:
            deletePB = QtWidgets.QPushButton()
            deletePB.setText("Delete")

            editPB = QtWidgets.QPushButton()
            editPB.setText("Edit")

            lastRowIndex = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(lastRowIndex)
            print(lastRowIndex)
           
            self.ui.tableWidget.setItem(
                lastRowIndex, 0, QtWidgets.QTableWidgetItem(str(std[1]))
            )
           
            self.ui.tableWidget.setItem(
                lastRowIndex, 1, QtWidgets.QTableWidgetItem(std[2])
            )
           
            self.ui.tableWidget.setItem(
                lastRowIndex, 2, QtWidgets.QTableWidgetItem(str(std[3]))
            )
           
            self.ui.tableWidget.setItem(
                lastRowIndex, 3, QtWidgets.QTableWidgetItem(str(std[4]))
            )
            
            self.ui.tableWidget.setCellWidget(lastRowIndex, 4, deletePB)
            self.ui.tableWidget.setCellWidget(lastRowIndex, 5, editPB)

            deletePB.clicked.connect(lambda *args, id=std[0]: self.deleteStd(id))
            editPB.clicked.connect(lambda *args, stdObj=std: self.editStd(stdObj))

    def addStd(self):
        symbols = ["1","2","3","4","5","6","7","8","9"] # Can add more
        ProductID = ""
        for _ in range(5):
          ProductID += secrets.choice(symbols)
        
        Product = self.ui.ProducktName.text()
        BuyPrice = self.ui.BuPrice.text()
        floting = float(BuyPrice)
        selpricecalk = str((floting +(floting*20)/100))
        SelePrice =  selpricecalk
        

        self.model.store(
            "insert into cg( ProductID ,Product ,BuyPrice , SelePrice) values ('"
            + ProductID
            + "' , '"
            + Product
            + "' , '"
            + BuyPrice
            + "' , '"
            + SelePrice
            + "')"
        )
        self.rendercg()
        self.ui.ProducktName.setText("")
        self.ui.BuPrice.setText("")



    def AllAdd(self,ProductID):
        Product = self.ui.ProducktName.text()
        BuyPrice = self.ui.BuPrice.text()
        floting = float(BuyPrice)
        selpricecalk = str((floting +(floting*20)/100))
        SelePrice =  selpricecalk
       

    def deleteStd(self, id):
        self.model.store("delete from cg where id = " + str(id))
        self.rendercg()

    def editStd(self, std):
        self.ui.hiddenValue.setText(str(std[0]))
        self.ui.ProducktName.setText(std[1])
        self.ui.BuPrice.setText(std[3])
       
        self.ui.CgAddPB.hide()
        self.ui.CgEditPB.show()

        self.ui.CgEditPB.clicked.connect(lambda: self.updateStd())


    def updateStd(self):
        Product = self.ui.ProducktName.text()
        BuyPrice = self.ui.BuPrice.text()
        floting = float(BuyPrice)
        selpricecalk = str((floting +(floting*20)/100))
        SelePrice =  selpricecalk
    
        index = int(self.ui.hiddenValue.text())

        self.model.store(
            "update cg set Product= '"
            + Product
            + "', BuyPrice = '"
            + BuyPrice
            + "', SelePrice = '"
            + SelePrice
            + "' where id = "
            + str(index)
        )
        

        self.rendercg()
        self.ui.CgAddPB.show()
        self.ui.CgEditPB.hide()
        self.ui.ProducktName.setText("")
        self.ui.BuPrice.setText("")
       

