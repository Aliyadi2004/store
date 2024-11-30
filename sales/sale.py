from PyQt6 import QtWidgets
from Addings.Model import *

#text = 'cvh'
#name = f'matn ma {text} ast'
#name1 = 'matn ma %s ast' %text
#print(text,'\n',name,'\n',name1)


class SalesCls:
    def __init__(self, ui):
        self.ui = ui
        self.model = Model()
        
        

    def renderSales(self):
        print("salam")
        self.ui.tableWidget.setRowCount(0)
        stdList = self.model.restore("select ProductCode, ProductName ,Price,sales.Count,TotalPrice from sales")
        print(stdList)
        for std in stdList:
            deletePB = QtWidgets.QPushButton()
            deletePB.setText("Delete")

            lastRowIndex = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(lastRowIndex)
            print(lastRowIndex)
           
            self.ui.tableWidget.setItem(
                lastRowIndex, 0, QtWidgets.QTableWidgetItem(str(std[0]))
            )
           
            self.ui.tableWidget.setItem(
                lastRowIndex, 1, QtWidgets.QTableWidgetItem(std[1])
            )
           
            self.ui.tableWidget.setItem(
                lastRowIndex, 2, QtWidgets.QTableWidgetItem(str(std[2]))
            )
           
            self.ui.tableWidget.setItem(
                lastRowIndex, 3, QtWidgets.QTableWidgetItem(str(std[3]))
             )
            
            self.ui.tableWidget.setItem(
                lastRowIndex, 4, QtWidgets.QTableWidgetItem(str(std[4]))
            )
            
            self.ui.tableWidget.setCellWidget(lastRowIndex, 5, deletePB)
            deletePB.clicked.connect(lambda *args, id=std[0]: self.deleteStd(id))


    def SaleAdd(self):
        PdName = self.ui.SProCode.text()
        self.model.store(
           f"INSERT INTO sales (sales.ProductCode, sales.ProductName, sales.Price) SELECT anbar.PruductID, anbar.Produckt, anbar.SellPrice FROM anbar WHERE anbar.Produckt ='{PdName}' "

        )
        Saleprice = self.model.restore(f"select Price from sales WHERE sales.ProductName = '{PdName}'")
        lastRow = self.findlastrowDatabase()
        saleCount =self.ui.Scout.text()
        for intsellprice in Saleprice:
             sellpricee = int(intsellprice[0])
        
        INTsaleCount= int(saleCount)
        
        GamPrice= INTsaleCount*sellpricee
        self.model.store(
            f"update sales set Count='{INTsaleCount}' , TotalPrice ='{GamPrice}'  where id = {lastRow}")
        self.AnbarUpdate(saleCount,sellpricee)
        self.renderSales()
        
        
    def findlastrowDatabase(self):
            Ali = self.model.restore(
                  "SELECT ID FROM sales ORDER BY ID DESC LIMIT 1"
            )
            for selectlastrow in Ali:
                lastrow = int(selectlastrow[0])
                
            return(lastrow)
    


    def AnbarUpdate(self,count,Saleprice):
        PdName = self.ui.SProCode.text() 
        print(PdName)
        MainCount=self.model.restore(f"SELECT anbar.Count FROM anbar WHERE anbar.Produckt = '{PdName}'")
        print("salam")
        print(MainCount)
        print(type(MainCount))
        INTcount= int(count)


        for intsellprice in MainCount:
            sellpricee = int(intsellprice[0])


        UpdatetCount = sellpricee - INTcount
        UpdatetCountTotalprice = Saleprice * UpdatetCount
        print(UpdatetCountTotalprice)
        print(UpdatetCount)
        self.model.store(
            f"update anbar set anbar.Count='{UpdatetCount}' , anbar.GamPrice ='{UpdatetCountTotalprice}'  where anbar.Produckt ='{PdName}'")


        
    def Endfunc(self):
        self.model.store(
            "INSERT INTO historysales SELECT * FROM sales")
            
        print("tamam")
        
        self.model.store(
            "DELETE FROM sales")
        self.renderSales()
                
