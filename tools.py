import binascii
import json
import re
import hashlib
import pyaes
from os import path


#variables
file = "HermesData.json"
salt = "iU9{nWRx8*B5^4:U!d8k"
saltEncrypt = "x3HMcVP>76fk7c$>-uc-86U6p~,N3D"

#functions
def WriteFile(currentPassword, data, item):
    """
    Open the data file, decrypt it and write in datas selected
    :param currentPassword: user password
    :param data: data to write
    :param item: wich data write in the file
    :return: binary in str
    """
    #write all the file
    if item == "datas":
        with open(file, 'w') as json_file:
            json.dump(data, json_file)
    #write a part of the file
    else:
        fullDatas = ReadFile(currentPassword, "datas")
        #write contacts
        if item == "contacts":
            datas = fullDatas['datas']
            datas['contacts'] = data
        #encryption of the file
        datasEncrypt = toAES(str(datas), toPasswordEncode(currentPassword))
        fullDatas['datas'] = datasEncrypt
        with open(file, 'w') as json_file:
            json.dump(fullDatas, json_file)

def ReadFile(currentPassword, item):
    """
    Get datas in the file
    :param currentPassword: user password
    :param item: wich data get
    :return: json data
    """
    with open(file) as fp:
        dataFile = json.load(fp)
    #return the hash of the file
    if item == "hash":
        return dataFile['hash']
    elif (dataFile['datas']):
        password = toPasswordEncode(currentPassword).encode('utf-8')
        aes = pyaes.AESModeOfOperationCTR(password)
        #decrypted data is always binary, need to decode to plaintext
        datasDecrypt = aes.decrypt(bytes.fromhex(dataFile['datas'])).decode('utf-8')
        datasJson = json.loads(datasDecrypt.replace("\'", "\""))
        #return all datas
        if item == "datas":
            fullData = {"hash": dataFile['hash'], 'datas': datasJson}
            return fullData
        #return contacts
        if item == "contacts":
            return datasJson['contacts']

def toAES(plainText, password):
    """
    Encrypt data into AES
    :param plainText: original text
    :param password: password to encrypt text
    :return: Encrypted text in hexa
    """
    key = str(password).encode('utf-8')
    #password must be byte
    aes = pyaes.AESModeOfOperationCTR(key)
    #encrypt test in AES to hexa
    cipherText = aes.encrypt(plainText)
    return cipherText.hex()

def toSHA(password):
    """
    transform text into SHA
    :param password: original text
    :return: SHA in hexa
    """
    return hashlib.sha256(password.encode()).hexdigest()

def toPasswordEncode(password):
    """
    transform password into 16 bytes key to do AES256
    :param password: original password
    :return: 16 bytes key
    """
    key = toSHA(saltEncrypt+password)[:16]
    return key