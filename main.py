import connexionUI
import sys

import tools


def hermesUI_start():
    """
    Create and lunch the first window
    """
    app = connexionUI.QtWidgets.QApplication(sys.argv)
    MainWindow = connexionUI.QtWidgets.QMainWindow()
    uiMainWindow = connexionUI.Ui_connexion()
    uiMainWindow.setupUi(MainWindow)
    sys.exit(app.exec_())


if __name__ == '__main__':
    hermesUI_start()