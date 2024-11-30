from PyQt6 import QtWidgets
from Addings.Model import *


class AnbarAddcls:
    def __init__(self, ui):
        self.ui = ui
        self.model = Model()
        
        

    def renderAnbar(self):
        self.ui.tableWidget.setRowCount(0)
        stdList = self.model.restore("select id, userID , UserName, Phonumber , Adress , PruductID , Produckt , SellPrice , Count , Datei , GamPrice from Anbar")

        for std in stdList:
            deletePB = QtWidgets.QPushButton()
            deletePB.setText("Delete")


            lastRowIndex = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(lastRowIndex)
            print(lastRowIndex)
           
            self.ui.tableWidget.setItem(
                lastRowIndex, 0, QtWidgets.QTableWidgetItem(std[1])
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
            self.ui.tableWidget.setItem(
                lastRowIndex, 5, QtWidgets.QTableWidgetItem(std[6])
            )
            self.ui.tableWidget.setItem(
                lastRowIndex, 6, QtWidgets.QTableWidgetItem(str(std[7]))
            )
            self.ui.tableWidget.setItem(
                lastRowIndex, 7, QtWidgets.QTableWidgetItem(str(std[8]))
            )
            self.ui.tableWidget.setItem(
                lastRowIndex, 8, QtWidgets.QTableWidgetItem(std[9])
            )
            self.ui.tableWidget.setItem(
                lastRowIndex, 9, QtWidgets.QTableWidgetItem(str(std[10]))
            )
            
            self.ui.tableWidget.setCellWidget(lastRowIndex, 10, deletePB)
            

            deletePB.clicked.connect(lambda *args, id=std[0]: self.deleteStd(id))
           




    def addusers(self):
        userid = self.ui.AnbarUserID.text()
        
        self.model.store(
            f"INSERT INTO anbar(userID ,UserName ,Phonumber , Adress) SELECT cpr.Userid, cpr.BuyersName, cpr.PhoneNumber, cpr.Adress FROM cpr WHERE cpr.Userid={userid}"
        )
        # print("khd")
        self.findlastrowDatabase()      
  

    def findlastrowDatabase(self):
        Ali = self.model.restore(
              "SELECT ID FROM anbar ORDER BY ID DESC LIMIT 1"
        )
        for selectlastrow in Ali:
            lastrow = int(selectlastrow[0])
            
        self.Addproduct(lastrow)
        


    def Addproduct(self,lastrow):
        producktid = self.ui.AnbarProducID.text()
        self.model.store(
              f"UPDATE anbar SET anbar.PruductID = (SELECT cg.ProductID FROM cg WHERE cg.ProductID = {producktid}), anbar.Produckt = (SELECT cg.Product FROM cg WHERE cg.ProductID = {producktid}), anbar.SellPrice = (SELECT cg.SelePrice FROM cg WHERE cg.ProductID = {producktid}) WHERE anbar.ID ={lastrow};"
         )
        self.Infos(lastrow)
 
 
 
 
    def Infos(self,lastrow):
        print(lastrow)
        producktid = self.ui.AnbarProducID.text()
        buycount =self.ui.AnbarCount.text()
        Datum =self.ui.AnbarTarikh.text()
        Ssellprice =  self.model.restore(
              f"SELECT cg.SelePrice FROM cg WHERE cg.ProductID ={producktid}"
        )        
        print(type(Ssellprice))
        print("sa;a,")
        for intsellprice in Ssellprice:
            sellpricee = int(intsellprice[0])
    
        INTbuycount= int(buycount)
        GamPrice= INTbuycount*sellpricee
        sellprice= str(sellpricee)
        self.Addcoutandelse(lastrow,sellprice,buycount,Datum,GamPrice)



    def Addcoutandelse(self,lastrow,sellprice,buycount,Datum,GamPrice):
       
        self.model.store(
            "update anbar set SellPrice= '"
            + str(sellprice)
            + "', Count = '"
            + str(buycount)
            + "', Datei = '"
            + str(Datum)
            + "', GamPrice = '"
            + str(GamPrice)
            + "' where id = "
            + str(lastrow)
        )
        self.renderAnbar()
  
    def deleteStd(self, id):
        self.model.store("delete from anbar where id = " + str(id))
        self.renderAnbar()

    # def editStd(self, std):
    #     self.ui.hiddenValue.setText(str(std[0]))
    #     self.ui.ProducktName.setText(std[1])
    #     self.ui.BuPrice.setText(std[3])
       
        


    #     self.ui.CgAddPB.hide()
    #     self.ui.CgEditPB.show()

    #     self.ui.CgEditPB.clicked.connect(lambda: self.updateStd()

