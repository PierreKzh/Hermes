# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pierre\Desktop\HermesPY\addContact.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
from PyQt5 import QtWidgets, QtCore, QtGui
import tools


class Ui_home(object):
    def setupUi(self, homeWindow, password):
        homeWindow.setObjectName("MainWindow")
        homeWindow.resize(801, 534)
        self.centralwidget = QtWidgets.QWidget(homeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 7, 1, 1)
        self.listWidget_contacts = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_contacts.setMinimumSize(QtCore.QSize(250, 0))
        self.listWidget_contacts.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget_contacts.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_contacts.setObjectName("listWidget_contacts")
        self.gridLayout_2.addWidget(self.listWidget_contacts, 3, 0, 1, 1)
        self.pushButton_AddContact = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AddContact.setObjectName("pushButton_AddContact")
        self.gridLayout_2.addWidget(self.pushButton_AddContact, 1, 0, 1, 1)
        self.pushButton_Profil = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Profil.setObjectName("pushButton_Profil")
        self.gridLayout_2.addWidget(self.pushButton_Profil, 0, 0, 1, 1)
        self.lineEdit_Research = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit_Research.setFont(font)
        self.lineEdit_Research.setText("")
        self.lineEdit_Research.setClearButtonEnabled(False)
        self.lineEdit_Research.setObjectName("lineEdit_Research")
        self.gridLayout_2.addWidget(self.lineEdit_Research, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Username = QtWidgets.QLabel(self.centralwidget)
        self.label_Username.setObjectName("label_Username")
        self.horizontalLayout.addWidget(self.label_Username)
        self.lineEdit_Username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.horizontalLayout.addWidget(self.lineEdit_Username)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.label_UsernameEvent = QtWidgets.QLabel(self.centralwidget)
        self.label_UsernameEvent.setText("")
        self.label_UsernameEvent.setObjectName("label_UsernameEvent")
        self.horizontalLayout_7.addWidget(self.label_UsernameEvent)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_IPaddress = QtWidgets.QLabel(self.centralwidget)
        self.label_IPaddress.setObjectName("label_IPaddress")
        self.horizontalLayout_2.addWidget(self.label_IPaddress)
        self.lineEdit_IPaddress = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_IPaddress.setObjectName("lineEdit_IPaddress")
        self.horizontalLayout_2.addWidget(self.lineEdit_IPaddress)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.label_IPaddressEvent = QtWidgets.QLabel(self.centralwidget)
        self.label_IPaddressEvent.setText("")
        self.label_IPaddressEvent.setObjectName("label_IPaddressEvent")
        self.horizontalLayout_6.addWidget(self.label_IPaddressEvent)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_Add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.horizontalLayout_3.addWidget(self.pushButton_Add)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 4, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.listWidget_MessageLeft = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_MessageLeft.setObjectName("listWidget_MessageLeft")
        self.horizontalLayout_9.addWidget(self.listWidget_MessageLeft)
        self.listWidget_MessageRight = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_MessageRight.setObjectName("listWidget_MessageRight")
        self.horizontalLayout_9.addWidget(self.listWidget_MessageRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_Message = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Message.setObjectName("lineEdit_Message")
        self.horizontalLayout_8.addWidget(self.lineEdit_Message)
        self.pushButton_Send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Send.setObjectName("pushButton_Send")
        self.horizontalLayout_8.addWidget(self.pushButton_Send)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 3, 4, 1)
        homeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(homeWindow)
        self.statusbar.setObjectName("statusbar")
        homeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(homeWindow)
        QtCore.QMetaObject.connectSlotsByName(homeWindow)

        #add action for list of members
        self.listWidget_contacts.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.actionDelete = QAction("Delete", self.listWidget_contacts)
        self.listWidget_contacts.addAction(self.actionDelete)
        #add function for an action in list members
        self.actionDelete.triggered.connect(lambda _, s=self: deleteContact(s))
        #display members list in the widget list contact
        self.currentPassword = password
        displayListWidget_contacts(self)
        #add contact pushing the buttun
        self.pushButton_Add.clicked.connect(lambda _, s=self: addContact(s))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_AddContact.setText(_translate("MainWindow", "Add contact"))
        self.pushButton_Profil.setText(_translate("MainWindow", "Profil"))
        self.lineEdit_Research.setPlaceholderText(_translate("MainWindow", "Research"))
        self.label_Username.setText(_translate("MainWindow", "Username : "))
        self.label_IPaddress.setText(_translate("MainWindow", "IP address : "))
        self.pushButton_Add.setText(_translate("MainWindow", "Add"))
        self.lineEdit_Message.setPlaceholderText(_translate("MainWindow", "Send message"))
        self.pushButton_Send.setText(_translate("MainWindow", "Send"))

def addContact(self):
    """
    Add contact in the file
    :param self: window parameters
    """
    #get the current contacts list
    listContact = tools.ReadFile(self.currentPassword, "contacts")
    #regex to verify ip address
    ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    #get informations
    self.Username = str(self.lineEdit_Username.text())
    self.IPaddress = str(self.lineEdit_IPaddress.text())
    #check informations
    if (self.Username != '' and self.IPaddress != ''):
        if(tools.re.match(ValidIpAddressRegex,self.IPaddress)):
            #add the contact to th list
            listContact.append({"Username": self.Username, "IPaddress": self.IPaddress})
            #write the data
            tools.WriteFile(self.currentPassword, listContact, "contacts")
            self.lineEdit_Username.setText('')
            self.lineEdit_IPaddress.setText('')
            #refresh the contact list in the window
            displayListWidget_contacts(self)
            self.label_IPaddressEvent.setText('')
        else:
            self.label_IPaddressEvent.setStyleSheet("color: red")
            self.label_IPaddressEvent.setText("Invalid IP address")

def deleteContact(self):
    """
    delete contact in the file
    :param self: window parameters
    """
    #get current contacts list
    listContact = tools.ReadFile(self.currentPassword, "contacts")
    newListContact = []
    row = self.listWidget_contacts.currentRow()
    i = len(listContact)-1
    #recreate the list without the deleted one
    for contact in listContact:
        if i != row:
            newListContact.append(contact)
        i-=1
    #write the file
    tools.WriteFile(self.currentPassword, newListContact, "contacts")
    #refresh the contact list in the window
    displayListWidget_contacts(self)

def displayListWidget_contacts(self):
    """
    Read contacts in the file and display it in the window
    :param password: original text
    """
    #get contacts list
    listContact = tools.ReadFile(self.currentPassword, "contacts")
    #clear the widget list
    self.listWidget_contacts.clear()
    #display contacts usernames
    for contact in listContact:
        self.listWidget_contacts.insertItem(0, contact['Username'])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeWindow = QtWidgets.QMainWindow()
    ui = Ui_home()
    ui.setupUi(homeWindow)
    homeWindow.show()
    sys.exit(app.exec_())