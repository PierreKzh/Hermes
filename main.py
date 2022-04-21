import tools
from connexionUI import *
from tools import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
    ##################################
    # SUPPRIMER LES THREADS A LA FIN #
    ##################################
    try:
        GUI = Thread(target=hermesUI_start)
        server = Thread(target=tools.communication.listenMessage, args=[s])
        torClient = Thread(target=tools.communication.torClient())
        GUI.setDaemon(True)
        server.setDaemon(True)
        torClient.setDaemon(True)

        GUI.start()
        server.start()
        torClient.start()
        while GUI.is_alive():
            pass
    except:
        print("==============ERROR WHEN LUNCHING APP==============")
    finally:
        print("===========CLOSE===============")