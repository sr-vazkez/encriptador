from cryptography.fernet import Fernet
import os


def retornarkey():
    '''
         Funcion retornarkey 
         Nos retorna el valor del key 
    '''
    return open("key.key", "rb").read()


def decrypt(items, key):
    """
         Funcion encrypt 
         Nos ayuda a generar lo necesario para generar la encriptacion de los
         archivos
    """
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data = file.read()
        data = i.decrypt(file_data)
        with open(x, "wb") as file:
            file.write(data)


if __name__ == "__main__":

    # En la siguiente linea se debe de escribir la ruta de los archivos a encryptar
    # Dependiendo el sistema ooperativo descomentar codigo
    # Ejemplo MacOs y Linux
    archivos = '/Users/papichiludo/Desktop/xdxdx'
    os.remove(archivos+"//"+"leeme.txt")
    items = os.listdir(archivos)
    archivos_2 = [archivos + "//" + x for x in items]
    # Ejemplo Windows
    #archivos = 'C:\\Users\\'
    # os.remove(archivos+"\\"+"leeme.txt")
    #items = os.listdir(archivos)
    #archivos_2 = [archivos + "\\" + x for x in items]

key = retornarkey()
decrypt(archivos_2, key)
