# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pierre\Desktop\HermesPY\addContact.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtWidgets import QWidget, QAction
from PyQt5 import QtWidgets, QtCore
from main import addContact, deleteContact, displayListWidget_contacts


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget_contacts = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_contacts.setMinimumSize(QtCore.QSize(250, 0))
        self.listWidget_contacts.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget_contacts.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.listWidget_contacts.setObjectName("listWidget_contacts")
        self.gridLayout_2.addWidget(self.listWidget_contacts, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
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
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.label_UsernameEvent = QtWidgets.QLabel(self.centralwidget)
        self.label_UsernameEvent.setText("")
        self.label_UsernameEvent.setObjectName("label_UsernameEvent")
        self.horizontalLayout_7.addWidget(self.label_UsernameEvent)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
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
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.label_IPaddressEvent = QtWidgets.QLabel(self.centralwidget)
        self.label_IPaddressEvent.setText("")
        self.label_IPaddressEvent.setObjectName("label_IPaddressEvent")
        self.horizontalLayout_6.addWidget(self.label_IPaddressEvent)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_Add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.horizontalLayout_3.addWidget(self.pushButton_Add)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 0, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #add action for list of members
        self.actionDelete = QAction("Delete", self.listWidget_contacts)
        self.listWidget_contacts.addAction(self.actionDelete)
        #add function for an action in list members
        self.actionDelete.triggered.connect(lambda _, s=self: deleteContact(s))
        #display members list in the widget list contact
        displayListWidget_contacts(self)
        #add contact pushing the buttun
        self.pushButton_Add.clicked.connect(lambda _, s=self: addContact(s))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Username.setText(_translate("MainWindow", "Username : "))
        self.label_IPaddress.setText(_translate("MainWindow", "IP address : "))
        self.pushButton_Add.setText(_translate("MainWindow", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())