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
from datetime import datetime as dt
import re
from pathlib import Path
import secrets
import os

sharedPassword = ""
userId = 0
dataBase = "dataFile.db"
sharedPublicKey = ""
sharedOnionAddress = ""

class crypto(object):
    fle = Path('salt.txt')
    fle.touch(exist_ok=True)
    f = open(fle, 'w+')
    if os.stat(fle).st_size == 0:
        salt_file = secrets.token_hex(16)
        f.write(salt_file)

    salt = f.read()
    f.close

    def encrypted(self, password, data):
        """
        It takes a password and data, and returns the encrypted data
        
        :param password: The password to use for encryption
        :param data: The data to be encrypted
        :return: The encrypted data.
        """
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
        """
        The function takes a password and a data string as input, and returns the decrypted data string
        
        :param password: The password to use for encryption
        :param data: The data to be encrypted
        :return: The decrypted data
        """
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

    def encrypt_RSA(self, pubKey, msg):
        """
        It encrypts the message using the public key.
        
        :param pubKey: The public key of the recipient
        :param msg: The message to be encrypted
        :return: The encrypted message.
        """
        encryptor = PKCS1_OAEP.new(pubKey)
        encrypted = encryptor.encrypt(msg)
        return encrypted

    def decrypt_RSA(self, keyPair, encrypted):
        """
        It decrypts the encrypted message using the private key.
        
        :param keyPair: The RSA key pair to use for decryption
        :param encrypted: The encrypted message
        :return: The decrypted message.
        """
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

    def send(torAddress, message):
        """
        It sends a message to a tor address.
        
        :param torAddress: the address of the contact
        :param message: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
        """
        print("========START SEND==========")
        try:
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", communication.internalPortClient, True)
            s = socks.socksocket()
            s.connect((torAddress, communication.externalPortServer))
            s.sendall(message)
            print("========END SEND========")
        except:
            print("=======SENDING MEMORY=========")
            encrypted_torAddress = crypto().encrypted(sharedPassword, torAddress)
            encrypted_message = crypto().encrypted(sharedPassword, binascii.hexlify(message).decode('utf-8'))
            encrypted_userId = crypto().encrypted(sharedPassword, str(userId))
            # Connection to the database
            conn = sqlite3.connect(dataBase)
            cursor = conn.cursor()

            # put paramaters in sending memory table
            cursor.execute(f"INSERT INTO sendingMemory (user_id, message, contact_address) VALUES ('{encrypted_userId}', '{encrypted_message}', '{encrypted_torAddress}')")
            conn.commit()
            print("=======SENDING MEMORY END=========")

    def retrySend():
        """
        It connects to the database, gets the data, decrypts it, and then sends it to the contact
        address.
        """
        print("========START RETRY SEND==========")
        while True:
            # Connection to the database
            conn = sqlite3.connect(dataBase)
            cursor = conn.cursor()

            # get privateKey
            cursor.execute('SELECT sm_id, user_id, message, contact_address FROM sendingMemory')
            rows = cursor.fetchall()
            for row in rows:
                db_smId = row[0]
                db_userId = row[1]
                decrypt_userId = crypto().decrypted(sharedPassword, db_userId)
                db_message = row[2]
                decrypt_message = crypto().decrypted(sharedPassword, db_message)
                db_contactAddress = row[3]
                decrypt_contactAddress = crypto().decrypted(sharedPassword, db_contactAddress)
                if(str(decrypt_userId) == str(userId)):
                    messageToSend = binascii.unhexlify(bytes(decrypt_message, 'utf-8'))
                    try:
                        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", communication.internalPortClient, True)
                        s = socks.socksocket()
                        s.connect((decrypt_contactAddress, communication.externalPortServer))
                        s.sendall(messageToSend)
                        print(f"===========MESSAGE SEND TO : {decrypt_contactAddress}")
                        cursor.execute(f"DELETE FROM sendingMemory WHERE sm_id = '{db_smId}'")

                    except:
                        print(f"==========MESSAGE NOT SEND TO : {decrypt_contactAddress}")
            conn.commit()
            time.sleep(10)

    def listenMessage(socket):
        """
        The function listenMessage() is a function that listens for incoming messages from the client
        
        :param socket: the socket object
        """
        try:
            userPrivateKey = ""
            CREATE_NO_WINDOW = 0x08000000

            print("===========START SERVER LISTENING============")
            pathExe = os.getcwd() + "\\hermesTor\\Tor\\tor.exe"
            pathConf = os.getcwd() + "\\hermesTor\\Data\\Server\\torrc"
            proc = subprocess.Popen([pathExe, "-f", pathConf], creationflags=CREATE_NO_WINDOW)
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
                    communication.checkCode(response, userId)

                    #client.send(b'{"replyCode":1}')
                    client.close()
                    time.sleep(0.5)
                    print("=========CONNECTION CLOSED============")
        except:
            print("============ERROR WHEN SERVER LISTENING================")

    def checkCode(response, userId):
        print("==========CHECK CODE============")
        try:
            response_json = json.loads(response)
            code = json.dumps(response_json["sendCode"])

            if int(code) == 100: # a message to an user
                message = json.loads(json.dumps(response_json["value"]))
                torAddress = json.loads(json.dumps(response_json["torAddress"]))
                communication.receiveMessage(message, torAddress, userId)

            if int(code) == 200: # ask to verif him in contacts
                hashed_publicKey = json.loads(json.dumps(response_json["publicKeyHash"]))
                getVerifContact(hashed_publicKey)

            if int(code) == 210: # you can deblock him in contacts
                hashed_publicKey = json.loads(json.dumps(response_json["publicKeyHash"]))
                setWaitingOk(hashed_publicKey)
        except:
            print("=========ERROR CHECK CODE========")

    def replyVerifContact(contactPublicKey, contactTorAddress):
        """
        ReplyVerifContact(contactPublicKey, contactTorAddress)
        
        :param contactPublicKey: The public key of the contact
        :param contactTorAddress: the tor address of the contact
        """
        print("============SEND REPLY VERIF CONTACT===========")
        try:
            # encrypt message
            jsonMessage = '{"sendCode":210, "publicKeyHash":"' + crypto().toSHA(sharedPublicKey) + '"}'
            import_pubKey = RSA.importKey(bytes(contactPublicKey, 'utf-8'))
            jsonMessageEncrypt = crypto().encrypt_RSA(import_pubKey, bytes(jsonMessage, 'utf-8'))

            # send message
            communication.send(contactTorAddress, jsonMessageEncrypt)
            print("=======END SEND REPLY VERIF CONTACT===========")
        except:
            print("==========ERROR SEND REPLY VERIF CONTACT============")

    def receiveMessage(message, torAddress, userId):
        """
        It receives a message, the tor address of the sender and the user id of the receiver
        
        :param message: the message received
        :param torAddress: the address of the sender
        :param userId: 1
        """
        print(message)
        print(torAddress)
        print(userId)
        # Connection to the database
        conn = sqlite3.connect(dataBase)
        cursor = conn.cursor()

        # contact username
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        for row in rows:
            decrypted_contactOnion = crypto().decrypted(sharedPassword, row[3])
            if decrypted_contactOnion == torAddress:
                contactId = row[0]
                contactUsername = row[2]
        conn.commit()
        print(userId)
        print(contactId)
        print(contactUsername)
        

        # id Conversation
        cursor.execute("SELECT * FROM conversations")
        rows = cursor.fetchall()
        for row in rows:
            decrypted_userId = crypto().decrypted(sharedPassword, row[1])
            decrypted_contactId = crypto().decrypted(sharedPassword, row[2])
            
            if decrypted_contactId == str(contactId) and decrypted_userId == str(userId):
                crypted_conversationId = crypto().encrypted(sharedPassword, str(row[0]))
        conn.commit()

        print(crypted_conversationId)

        # signal for receive message
        cryptedSenderDirection = crypto().encrypted(sharedPassword, "receive")
        print(cryptedSenderDirection)

        communication.insertMessageDatabase(cryptedSenderDirection, message, contactUsername, crypted_conversationId)

        print(f"==========GET MESSAGE : {message}, from {torAddress}===========")
        
    def sendMessage(message, torAddress, userId):
        """
        It takes a message, a tor address, and a user id, and then it sends the message to the tor
        address
        
        :param message: the message to be sent
        :param torAddress: The onion address of the contact
        :param userId: the id of the user who is sending the message
        """
        # Connection to the database
        conn = sqlite3.connect(dataBase)
        cursor = conn.cursor()

        # contact username
        cursor.execute(f"SELECT * FROM users WHERE user_id = '{userId}'")
        rows = cursor.fetchall()
        for row in rows:
            userUsername = crypto().decrypted(sharedPassword, row[1])
        conn.commit()
        crypted_userUsername = crypto().encrypted(sharedPassword, userUsername)

        # contact username
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        for row in rows:
            decrypted_contactOnion = crypto().decrypted(sharedPassword, row[3])
            if decrypted_contactOnion == torAddress:
                contactId = row[0]
                contactUsername = row[2]
        conn.commit()
        
        # id Conversation
        cursor.execute("SELECT * FROM conversations")
        rows = cursor.fetchall()
        for row in rows:
            decrypted_userId = crypto().decrypted(sharedPassword, row[1])
            decrypted_contactId = crypto().decrypted(sharedPassword, row[2])
            
            if decrypted_contactId == str(contactId) and decrypted_userId == str(userId):
                crypted_conversationId = crypto().encrypted(sharedPassword, str(row[0]))
        conn.commit()

        # signal for receive message
        cryptedSenderDirection = crypto().encrypted(sharedPassword, "send")

        communication.insertMessageDatabase(cryptedSenderDirection, message, crypted_userUsername, crypted_conversationId)

    def torClient():
        """
        It starts the tor client and sets the proxy to 127.0.0.1:internalPortClient
        """
        try:
            print("=============START TOR CLIENT=================")
            CREATE_NO_WINDOW = 0x08000000

            pathExe = os.getcwd() + "\\hermesTor\\Tor\\tor.exe"
            pathConf = os.getcwd() + "\\hermesTor\\Data\\Client\\torrc"
            subprocess.Popen([pathExe, "-f", pathConf], creationflags=CREATE_NO_WINDOW)
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", communication.internalPortClient, True)
            print("============TOR CLIENT SET==================")
        except:
            print("============ERROR WHEN TOR CLIENT STARTING============")

    def insertMessageDatabase(direction, message, username, conversation_id):
        """
        It inserts a message into a database.
        
        :param direction: 0 for incoming, 1 for outgoing
        :param message: the message to be inserted
        :param username: The username of the person who sent the message
        :param conversation_id: The id of the conversation
        """
        print("============INSERT MESSAGE IN DATABASE==================")
        # Connection to the database
        conn = sqlite3.connect(dataBase)
        cursor = conn.cursor()
    
        # message
        message = crypto().encrypted(sharedPassword, message)

        # time
        now = dt.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        date = crypto().encrypted(sharedPassword, date)

        # add conversation
        cursor.execute(f"INSERT INTO messages (conversation_id, sender_direction, sender_username, date, message) VALUES ('{conversation_id}', '{direction}', '{username}', '{date}', '{message}')")
        conn.commit()
        

def getVerifContact(hashed_publicKey):
    """
    It takes a hashed public key as an argument, and then it calls the setWaitingOk function, which
    returns a tor address and a public key. If the tor address is not 0, then it calls the
    replyVerifContact function, which takes the public key and the tor address as arguments
    
    :param hashed_publicKey: the public key of the contact you want to verify
    """
    print("==========GET VERIF CONTACT==========")
    try:
        torAdress, publicKey = setWaitingOk(hashed_publicKey)
        if(torAdress != 0):
            communication.replyVerifContact(publicKey, torAdress)
        print("=========END GET VERIF CONTACT=========")
    except:
        print("==========ERROR GET VERIF CONTACT============")

def setWaitingOk(hashed_publicKey):
    """
    It takes a hashed public key as input, and returns the decrypted tor address and public key of the
    contact with the same hashed public key
    
    :param hashed_publicKey: the public key of the contact, hashed with SHA256
    :return: the decrypted torAddress and decrypted publicKey.
    """
    print("=======SET WAITING TO 1=========")
    try:
        # verification du contact dans la bdd
        # Connection to the database
        conn = sqlite3.connect(dataBase)
        cursor = conn.cursor()

        cursor.execute('SELECT contact_id, contact_onion, contact_publicKey, waiting FROM contacts')
        rows = cursor.fetchall()
        for row in rows:
            db_contactID = row[0]
            db_torAddress = row[1]
            decrypt_torAddress = crypto().decrypted(sharedPassword, db_torAddress)
            db_publicKey = row[2]
            decrypt_publicKey = crypto().decrypted(sharedPassword, db_publicKey)
            if hashed_publicKey == crypto().toSHA(decrypt_publicKey):
                waitingValue = crypto().encrypted(sharedPassword, "0")
                cursor.execute(f'UPDATE contacts SET waiting = "{waitingValue}" WHERE contact_id = {db_contactID}')
                conn.commit()
                print("========END SET WAITING===========")
                return decrypt_torAddress, decrypt_publicKey
        return 0, 0
    except:
        print("========ERROR WHEN SET WAITING CONTACT=========")
