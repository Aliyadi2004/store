from PyQt6 import QtWidgets
from Addings.Model import *
import secrets


class CprAdd:
    def __init__(self, ui):
        self.ui = ui
        self.model = Model()
        
        

    def rendercpr(self):
        self.ui.tableWidget.setRowCount(0)
        stdList = self.model.restore("select id, Userid ,BuyersName, PhoneNumber, Adress, Dati from cpr")

        for std in stdList:
            deletePB = QtWidgets.QPushButton()
            deletePB.setText("delete")

            editPB = QtWidgets.QPushButton()
            editPB.setText("edit")

            lastRowIndex = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(lastRowIndex)
            
            self.ui.tableWidget.setItem(
                lastRowIndex, 0, QtWidgets.QTableWidgetItem(str(std[1]))
            )
            
            self.ui.tableWidget.setItem(
                lastRowIndex, 1, QtWidgets.QTableWidgetItem(std[2])
            )
            
            self.ui.tableWidget.setItem(
                lastRowIndex, 2, QtWidgets.QTableWidgetItem(std[3])
            )
            
            self.ui.tableWidget.setItem(
                lastRowIndex, 3, QtWidgets.QTableWidgetItem(std[4])
            )
            
            self.ui.tableWidget.setItem(
                lastRowIndex, 4, QtWidgets.QTableWidgetItem(std[5])
            )
            
            self.ui.tableWidget.setCellWidget(lastRowIndex, 5, deletePB)
            self.ui.tableWidget.setCellWidget(lastRowIndex, 6, editPB)

            deletePB.clicked.connect(lambda *args, id=std[0]: self.deleteStd(id))
            editPB.clicked.connect(lambda *args, stdObj=std: self.editStd(stdObj))

    def addStd(self):
        symbols = ["1","2","3","4","5","6","7","8","9"] # Can add more
        Userid = ""
        for _ in range(5):
          Userid += secrets.choice(symbols)

        print(Userid)
        BuyersName = self.ui.NameKh.text()
        PhoneNumber = self.ui.shomareh.text()
        Adres = self.ui.Adres.text() 
        Dati = self.ui.tarikh.text()

        self.model.store(
            "insert into cpr( Userid ,BuyersName,  Dati , PhoneNumber , Adress) values ('"
            + Userid
            + "' , '"
            + BuyersName
            + "' , '"
            + Dati
            + "' , '"
            + PhoneNumber 
            + "' , '"
            + Adres
            + "')"
        )
        self.rendercpr()
        self.ui.NameKh.setText("")
        self.ui.shomareh.setText("")
        self.ui.Adres.setText("")
        self.ui.tarikh.setText("")






    def deleteStd(self, id):
        self.model.store("delete from cpr where id = " + str(id))
        self.rendercpr()

    def editStd(self, std):
        self.ui.hiddenValue.setText(str(std[0]))
        self.ui.NameKh.setText(std[2])
        self.ui.shomareh.setText(std[3])
        self.ui.Adres.setText(std[4])
        self.ui.tarikh.setText(std[5])


        self.ui.AddPB.hide()
        self.ui.EditPB.show()

        self.ui.EditPB.clicked.connect(lambda: self.updateStd())


    def updateStd(self):
        BuyersName = self.ui.NameKh.text()
        PhoneNumber = self.ui.shomareh.text()
        Adres = self.ui.Adres.text() 
        Dati = self.ui.tarikh.text()

        index = int(self.ui.hiddenValue.text())

        self.model.store(
            "update cpr set BuyersName= '"
            + BuyersName
            + "', Dati = '"
            + Dati
            + "', PhoneNumber = '"
            + PhoneNumber
            + "', Adress = '"
            + Adres
            + "' where id = "
            + str(index)
        )
        self.updateALL()
        self.rendercpr()
        self.ui.AddPB.show()
        self.ui.EditPB.hide()
        self.ui.NameKh.setText("")
        self.ui.shomareh.setText("")
        self.ui.Adres.setText("")
        self.ui.tarikh.setText("")


       
    def updateALL(self):
        BuyersName = self.ui.NameKh.text()
        PhoneNumber = self.ui.shomareh.text()
        Adres = self.ui.Adres.text() 
        Dati = self.ui.tarikh.text()

        index = int(self.ui.hiddenValue.text())

        self.model.store(
            "update cgandcpr set cprbuyername= '"
            + BuyersName
            + "', cprphonenamber = '"
            + PhoneNumber
            + "', cpradress = '"
            + Adres
            + "', cprdati = '"
            + Dati
            + "' where id = "
            + str(index)
        )

       