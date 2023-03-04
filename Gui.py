import bankdao as bankobj  #importing the bankdao file in this file

import sys #importing sys,pyqt5,qt6
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt6 import *
from PyQt6.QtWidgets import QLabel,QApplication,QVBoxLayout,QLineEdit,QWidget,QDialog,QMainWindow,QPushButton,QGridLayout
import PySide6
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.newobj=bankobj.tables()
        self.newobj.databasecreation() #creating connection to db
        #self.ww=QWidget()
        self.resize(400,400) #window size
        self.setWindowTitle("Bank of Baroda") # title
        self.layout=QGridLayout()
        self.setLayout(self.layout)

        title=QLabel("WELCOME \n Enter 1.REGISTER 2.LOGIN 0.Exit")  #label creationn
        self.layout.addWidget(title, 0,1,Qt.AlignmentFlag.AlignCenter)

        self.label0=QLabel("Choice",self)   
        self.layout.addWidget(self.label0,1,0)
        self.input0=QLineEdit()
        self.layout.addWidget(self.input0,1,1)

        bu2=QPushButton("GO")
        self.layout.addWidget(bu2,2,0,Qt.AlignmentFlag.AlignCenter)
        bu2.setFixedWidth(50)
        bu2.clicked.connect(self.a)

        self.label1=QLabel("Userid: ",self)
        self.label2=QLabel("Name: ",self)
        self.label3=QLabel("Phone: ",self)
        self. label4=QLabel("Place: ",self) 
        self.label11=QLabel("DONE",self)
        self.label5=QLabel('Enter user id')
        self.label18=QLabel("not enough baalnnce")

        self.input1=QLineEdit()
        self.input2=QLineEdit()
        self.input3=QLineEdit()
        self.input4=QLineEdit()



        self.name = ''
        self.nme = ''
        self.accbal = 0.0
        self.oldbal=0.0
       
        #self.ww.setWindowTitle("PyQt MessageBox")
       # bu2=QPushButton("Login")
        #layout.addWidget(bu2,5,2,Qt.AlignmentFlag.AlignLeft)
        #bu2.setFixedWidth(50)
    def a(self):
        ss=self.input0.text()        
        if ss=='0':
            print('EXIT')
        if ss=='1':       # s=1 go for the user register info
            self.label11.clear()
            self.layout.addWidget(self.label1,3,0)
            self.layout.addWidget(self.input1,3,1)
            self.layout.addWidget(self.label2,4,0)
            self.layout.addWidget(self.input2,4,1)
            self.layout.addWidget(self.label3,5,0)
            self.layout.addWidget(self.input3,5,1)
            self.layout.addWidget(self.label4,6,0)
            self.layout.addWidget(self.input4,6,1)
            self.label11=QLabel("Done")
            bu=QPushButton("Register") #button to submit the register data
            bu.setFixedWidth(50)
            bu.clicked.connect(self.display) #go to display function
            self.layout.addWidget(bu,7,1,Qt.AlignmentFlag.AlignRight)
            #for hiding purpose
            #self.layout.addWidget.hide()
            
            self.input0.clear()
            self.input1.clear()
            self.input2.clear()
            self.input3.clear()
            self.input4.clear()

            
        if ss=='2': #if s==2 goes for user account details updation
            self.label1.setHidden(True)
            self.layout.addWidget(self.label5,8,0)
            self.input5=QLineEdit()
            self.layout.addWidget(self.input5,8,1)
            bu3=QPushButton('Access') #button to enter user account updation
            bu3.setFixedWidth(50)
            bu3.clicked.connect(self.details) #ask the user what is ur option by the details method
            self.layout.addWidget(bu3,9,0,Qt.AlignmentFlag.AlignRight)
            
            self.label1.clear()
            self.label2.clear()
            self.label3.clear()
            self.label4.clear()
            self.label11.clear()
            self.input1.clear()
            self.input2.clear()
            self.input3.clear()
            self.input4.clear()
            
    def details(self):  #labels display to pick option from the user
        self.label6=QLabel("1.Deposit ")
        self.layout.addWidget(self.label6,10,0)
    
        self.label7=QLabel("2.Withdraw ")
        self.layout.addWidget(self.label7,11,0)
    

        self.label8=QLabel("3.Transfer ")
        self.layout.addWidget(self.label8,12,0)


        self. label9=QLabel("4.Balance ")
        self.layout.addWidget(self.label9,13,0)

        self. label10=QLabel("5.Transactions ")
        self.layout.addWidget(self.label10,14,0)

        self.input6=QLineEdit()
        self.layout.addWidget(self.input6,15,0)
        bu4=QPushButton('Do')
        bu4.setFixedWidth(50)
        bu4.clicked.connect(self.detail)
        self.layout.addWidget(bu4,16,0,Qt.AlignmentFlag.AlignRight)

    def detail(self):
        sk=self.input6.text()  #input from user 
        self.input6.clear()
        self.id=self.input5.text() #taking user id from above inputs
        self.id=int(self.id)
        self.newobj.calling(self.id)
        if sk=='1':  #asking user for depositing the money
            self.label12=QLabel("Enter Amount")
            self.layout.addWidget(self.label12,17,0)
            self.input7=QLineEdit()
            self.layout.addWidget(self.input7,17,1)
            bu5=QPushButton('Enter')
            bu5.setFixedWidth(50)
            bu5.clicked.connect(self.sun)
            self.layout.addWidget(bu5,17,2,Qt.AlignmentFlag.AlignRight)
        
            
            #self.amount=int(self.amount)
            #self.accbal = self.accbal+self.amount
            #self.info()
        elif sk=='2':  #asking user to withdraw the money amount
            self.label13=QLabel("withdraw amount")
            self.layout.addWidget(self.label13,18,0)
            self.input8=QLineEdit()
            self.layout.addWidget(self.input8,18,1)
            bu6=QPushButton('Enter')
            bu6.setFixedWidth(50)
            bu6.clicked.connect(self.sunn) #updation method
            self.layout.addWidget(bu6,18,2,Qt.AlignmentFlag.AlignRight)
        elif sk=='3': #asking for transferid and amount to make a transaction
            self.label14=QLabel("Transferid")
            self.layout.addWidget(self.label14,19,0)
            self.input9=QLineEdit()
            self.layout.addWidget(self.input9,19,1)
            self.trid=self.input9.text()
            self.label15=QLabel("Transfer amount")
            self.layout.addWidget(self.label15,20,0)
            self.input10=QLineEdit()
            self.layout.addWidget(self.input10,20,1)
            bu7=QPushButton('Transfer')
            bu7.setFixedWidth(50)
            bu7.clicked.connect(self.sunnn) #updation method 
            self.layout.addWidget(bu7,21,1,Qt.AlignmentFlag.AlignRight)

            

        elif sk=='4': #to display the user account balance
            self.newobj.chbln()
        elif sk=='5': #to display the user transactions history
            self.newobj.checktrans()
        else:
            pass
        


        

    def display(self):
        self.layout.addWidget(self.label11, 7,0,Qt.AlignmentFlag.AlignLeft)
        self.id=self.input1.text()
        name=self.input2.text()
        phone=self.input3.text()
        place=self.input4.text()
        self.newobj.register(self.id,name,phone,place)

    def sun(self):
        self.newobj.calling(self.id)
        self.amount =self.input7.text()
        self.amount=float(self.amount)
        self.newobj.deposit(self.amount)
        self.input7.clear()
        self.label12.clear()





    def sunn(self):
        self.newobj.databasecreation()
        self.newobj.calling(self.id)
        self.withdrawn=self.input8.text()
        self.withdrawn=float(self.withdrawn)
        #if self.accbal < self.withdrawn:
                #self.label17=QLabel("not enough baalnnce")
                #self.layout.addWidget(self.label17,21,0)
        #else:
        self.newobj.w_d(self.withdrawn)
        self.layout.addWidget(self.label11, 25,0,Qt.AlignmentFlag.AlignLeft)
        

        self.label13.clear()
        self.input8.clear()





    def sunnn(self):
        #self.newobj.databasecreation()
        self.newobj.calling(self.id)
        self.trid=self.input9.text()
        self.transfered=self.input10.text()
        self.newobj.trans(self.trid,self.transfered)
        self.layout.addWidget(self.label11, 25,0,Qt.AlignmentFlag.AlignLeft)

        
        self.label14.clear()
        self.input9.clear()
        self.label15.clear()
        self.input10.clear()
        self.label18.clear()

                
app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec())