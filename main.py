from cryptography.fernet import fernet
import os

def generateKey():
     '''
          Funcion 'Generar key'       
     '''
     key = Fernet.generate_key()
     with open("key.key", "wb") as key_file:
          key_file.write(key)

