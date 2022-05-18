import os, binascii, codecs
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from binascii import b2a_hex
import sys
import sqlite3
from threading import Thread
import subprocess
import socket
import time
import json
import socks
import hashlib
import pyaes
import datetime

sharedPassword = ""
userId = 0
dataBase = "dataFile.db"
sharedPublicKey = ""
sharedOnionAddress = ""

class crypto(object):
    salt = binascii.unhexlify('7d34f60be198c7397de94885a7489390')

    def encrypted(self, password, data):
        try:
            print("===CHIFFREMENT EN COURS===")
            # key must be bytes, so we convert it
            key = binascii.hexlify(PBKDF2(password, crypto.salt, dkLen=16))

            aes = pyaes.AESModeOfOperationCTR(key)
            ciphertext = aes.encrypt(data)

            print("===CHIFFREMENT TERMINE===")
            return ciphertext.hex()
        except:
            print("===CHIFFREMENT ERREUR===")

    def decrypted(self, password, data):
        print("===DECHIFFREMENT EN COURS===")
        try:
            # DECRYPTION
            # CRT mode decryption requires a new instance be created
            key = binascii.hexlify(PBKDF2(password, crypto.salt, dkLen=16))
            aes = pyaes.AESModeOfOperationCTR(key)

            # decrypted data is always binary, need to decode to plaintext
            decrypted = aes.decrypt(binascii.unhexlify(data)).decode('utf-8')
            print("===DECHIFFREMENT TERMINE===")
            return decrypted
        except:
            print("===DECHIFFREMENT ERREUR===")

    def encrypt_RSA(pubKey, msg):
        encryptor = PKCS1_OAEP.new(pubKey)
        encrypted = encryptor.encrypt(msg)
        return encrypted

    def decrypt_RSA(self, keyPair, encrypted):
        decryptor = PKCS1_OAEP.new(keyPair)
        decrypted = decryptor.decrypt(encrypted)
        return decrypted

    def toSHA(self, password):
        """
        transform text into SHA
        :param password: original text
        :return: SHA in hexa
        """
        return hashlib.sha256(password.encode()).hexdigest()

class communication(object):
    internalPortClient = 9060
    internalPortServer = 13710
    externalPortServer = 13711

    def listenMessage(socket):
        try:
            userPrivateKey = ""

            print("===========START SERVER LISTENING============")
            pathExe = os.getcwd() + "\\hermesTor\\Tor\\tor.exe"
            pathConf = os.getcwd() + "\\hermesTor\\Data\\Server\\torrc"
            proc = subprocess.Popen([pathExe, "-f", pathConf])
            socket.bind(('', communication.internalPortServer))

            while True:
                socket.listen(5)
                client, address = socket.accept()
                encryptedResponse = client.recv(4096)
                print(f"=============SERVER CONNECTED TO : {format(address)}==============")
                if encryptedResponse != "":
                    # Connection to the database
                    conn = sqlite3.connect(dataBase)
                    cursor = conn.cursor()

                    # get privateKey
                    cursor.execute('SELECT user_id, private_key FROM users')
                    rows = cursor.fetchall()
                    for row in rows:
                        db_userId = row[0]
                        db_privateKey = row[1]
                        decrypt_privateKey = crypto().decrypted(sharedPassword, db_privateKey)
                        if db_userId == userId:
                            userPrivateKey = decrypt_privateKey.replace(r'\n', '\n')
                    conn.commit()

                    #decrypt message
                    import_privateKey = RSA.import_key(bytes(userPrivateKey, 'utf-8'))
                    response = crypto().decrypt_RSA(import_privateKey, encryptedResponse)
                    communication.checkCode(response)

                    #client.send(b'{"replyCode":1}')
                    client.close()
                    time.sleep(0.5)
                    print("=========CONNECTION CLOSED============")
        except:
            print("============ERROR WHEN SERVER LISTENING================")

    def checkCode(response):
        print("==========CHECK CODE============")
        try:
            response_json = json.loads(response)
            code = json.dumps(response_json["sendCode"])

            if int(code) == 100:
                message = json.loads(json.dumps(response_json["value"]))
                torAddress = json.loads(json.dumps(response_json["torAddress"]))
                communication.getMessage(message, torAddress)
        except:
            print("=========ERROR CHECK CODE========")

    def getMessage(message, torAddress):
        print("==========GET MESSAGE===========")
        try:
            # Connection to the database
            conn = sqlite3.connect('dataFile.db')
            cursor = conn.cursor()
            crypt = crypto()

            # get contact
            cursor.execute('SELECT contact_id, contact_onion FROM contacts')
            rows = cursor.fetchall()
            for row in rows:
                db_contactID = row[0]
                db_torAddress = row[1]
                decrypt_torAddress = crypt.decrypted(sharedPassword, db_torAddress)
                if torAddress == decrypt_torAddress:
                    now = datetime.datetime.now()
                    dateMessage = now.strftime("%d-%m-%Y %H:%M:%S")
                    encrypted_UserId = crypto().encrypted(sharedPassword, str(userId))
                    encrypted_contactId = crypto().encrypted(sharedPassword, str(db_contactID))
                    encrypted_dateMessage = crypto().encrypted(sharedPassword, str(dateMessage))
                    encrypted_message = crypto().encrypted(sharedPassword, str(message))
                    print("add bdd")
                    print(userId, db_contactID, dateMessage, message)
                    print(encrypted_UserId, encrypted_contactId, encrypted_dateMessage, encrypted_message)
                    break
            conn.commit()

            print(f"============MESSAGE GET : {message}============")
        except:
            print("=========ERROR GET MESSAGE============")


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