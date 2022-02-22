import addContactUI
import sys
import json
from os import path
import re

#variables
file = "HermesData.json"


#class
class Contact:
    def __init__(self, Username, IPaddress):
        self.Username = Username
        self.IPaddress = IPaddress

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


#functions
def hermesUI_start():
    app = addContactUI.QtWidgets.QApplication(sys.argv)
    MainWindow = addContactUI.QtWidgets.QMainWindow()
    ui = addContactUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def WriteFile(listContact):
        with open(file, 'w') as json_file:
            json.dump(listContact, json_file)

def ReadFile():
    with open(file) as fp:
        listContact = json.load(fp)
    return listContact

def addContact(self):
    listContact = ReadFile()
    ValidIpAddressRegex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
    self.Username = str(self.lineEdit_Username.text())
    self.IPaddress = str(self.lineEdit_IPaddress.text())
    if (self.Username != '' and self.IPaddress != ''):
        if(re.match(ValidIpAddressRegex,self.IPaddress)):
            listContact.append(Contact(self.Username, self.IPaddress).toJson())
            WriteFile(listContact)
            self.lineEdit_Username.setText('')
            self.lineEdit_IPaddress.setText('')
            displayListWidget_contacts(self)
            self.label_IPaddressEvent.setText('')
        else:
            self.label_IPaddressEvent.setStyleSheet("color: red")
            self.label_IPaddressEvent.setText("Invalid IP address")

def deleteContact(self):
    listContact = ReadFile()
    newListContact = []
    row = self.listWidget_contacts.currentRow()
    i = len(listContact)-1
    for contact in listContact:
        if i != row:
            newListContact.append(contact)
        else:
            print("on ajoute pas"+contact)
        i-=1
    WriteFile(newListContact)
    displayListWidget_contacts(self)

def displayListWidget_contacts(self):
    if path.isfile(file) is False:
        listContact = []
        with open(file, 'w') as json_file:
            json.dump(listContact, json_file)
    listContact = ReadFile()
    self.listWidget_contacts.clear()
    for contact in listContact:
        contact = Payload(contact)
        self.listWidget_contacts.insertItem(0, contact.Username)


#code


if __name__ == '__main__':
    hermesUI_start()
    """list = []
    list.append(Contact(Username="pierre", IPaddress="127.0.0.1").toJson())
    list.append(Contact(Username="JB", IPaddress="127.0.0.2").toJson())
    WriteFile(list)"""