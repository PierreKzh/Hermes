import os, binascii, codecs
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex
import sys
import sqlite3
from threading import Thread
import subprocess
import socket
import time
import json
import socks

class crypto(object):
    
    def encrypted(self, password, data):
        try:
            print("===CHIFFREMENT EN COURS===")
            iv = Random.new().read(AES.block_size)                          #IV
            salt = binascii.unhexlify('7d34f60be198c7397de94885a7489390')   # Salt
            key = binascii.hexlify(PBKDF2(password, salt, dkLen=16))        # Key
        
            # Use key and iv to initialize AES object
            mycipher = AES.new(key, AES.MODE_CFB, iv)

            # Add iv to the beginning of the encrypted ciphertext
            ciphertext = iv + mycipher.encrypt(str(data).encode())
            ciphertext = ciphertext.hex()

            print("===CHIFFREMENT TERMINE===")
            return ciphertext
        except:
            print("===CHIFFREMENT ERREUR===")
            return None


    def decrypted(self, password, data):
        try:
            print("===DECHIFFREMENT EN COURS===")
            salt = binascii.unhexlify('7d34f60be198c7397de94885a7489390')   # Salt
            key = binascii.hexlify(PBKDF2(password, salt, dkLen=16))        # Key
            data = binascii.unhexlify(data)                                 
        
            # Use key and iv to generate a new AES object
            mydecrypt = AES.new(key, AES.MODE_CFB, data[:16])

            # Decrypt the encrypted ciphertext
            decrypttext = mydecrypt.decrypt(data[16:])
            decrypttext = decrypttext.decode()

            print("===DECHIFFREMENT TERMINE===")
            return decrypttext
        except:
            print("===DECHIFFREMENT ERREUR===")
            return None
class communication(object):
    internalPortClient = 9060
    internalPortServer = 13710
    externalPortServer = 13711

    def listenMessage(socket):
        try:
            print("===========START SERVER LISTENING============")
            pathExe = os.getcwd() + "\\hermesTor\\Tor\\tor.exe"
            pathConf = os.getcwd() + "\\hermesTor\\Data\\Server\\torrc"
            proc = subprocess.Popen([pathExe, "-f", pathConf])
            socket.bind(('', communication.internalPortServer))

            while True:
                socket.listen(5)
                client, address = socket.accept()
                response = client.recv(255)
                print(f"=============SERVER CONNECTED TO : {format(address)}==============")
                if response != "":
                    response_json = json.loads(response)
                    message = json.dumps(response_json["value"])

                    client.send(b'{"replyCode":1}')
                    client.close()
                    time.sleep(0.5)
                    print(f"============MESSAGE GET : {message}=============")
                    print("=========CONNECTION CLOSED============")
        except:
            print("============ERROR WHEN SERVER LISTENING================")

    def torClient():
        try:
            print("=============START TOR CLIENT=================")
            pathExe = os.getcwd() + "\\hermesTor\\Tor\\tor.exe"
            pathConf = os.getcwd() + "\\hermesTor\\Data\\Client\\torrc"
            subprocess.Popen([pathExe, "-f", pathConf])
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", communication.internalPortClient, True)
            print("============TOR CLIENT SET==================")
        except:
            print("============ERROR WHEN TOR CLIENT STARTING============")


if __name__ == '__main__':
    password = 'password'
    text = 'message'

    crypto = crypto()
    encrypttext = crypto.encrypted(password, text)
    print("The encrypted data is: ",encrypttext)
    
    decrypttext = crypto.decrypted(password, encrypttext)
    print("The decrypted data is: ", decrypttext)
    
    print("Message : ", text)
    
    if text == decrypttext:
        print("OK")
        
    else:
        print("NOT")