import os, binascii, codecs
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex
import sys
import sqlite3

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