from cryptography.fernet import fernet
import os

def generateKey():
     '''
          Funcion 'Generar key' 
          Esta funcion nos genera un archivo con una contraseña      
     '''
     key = Fernet.generate_key()
     with open("key.key", "wb") as key_file:
          key_file.write(key)

