from connexionUI import *

def hermesUI_start():
    """
    Create and lunch the first window
    """
    print("========================HERMES START========================")
    app = QtWidgets.QApplication(sys.argv)
    connexion = QtWidgets.QMainWindow()
    uiConnect = Ui_connexion()
    uiConnect.setupUi(connexion)
    connexion.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    hermesUI_start()