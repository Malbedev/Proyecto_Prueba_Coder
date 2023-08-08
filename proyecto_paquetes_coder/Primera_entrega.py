
import re
import json
BD ={}

any_number_regex = '[0-9]'
any_capital_letter = '.*[A-Z].*'

def Registro(dict):
  usuario = input(str('ingrese un nombre de usuario: '))
  contraseña = input('Ingrese una contraseña: ')
  while True:
    if not  6<=len(contraseña.replace(' ',''))<=20:
      print('Su contraseña debe tener una Longitud entre 6 y 20 caracteres')
      contraseña = input('Ingrese una contraseña valida: ')
    if not re.search(any_number_regex,contraseña):
      print('A su contraseña le falta un caracter numerico')
      contraseña = input('Ingrese una contraseña valida: ')
    if not re.search(any_capital_letter,contraseña):
      print('A su contraseña le falta Caracteres en Mayuscula')
      contraseña = input('Ingrese una contraseña valida: ')
    else:
      BD.update({usuario:contraseña})
      
      break
  nuevo_ususario= input(str('Desea Ingresar otro usuario? SI/NO: '))
  if nuevo_ususario.lower() == 'si':
    Registro(dict)
  else:
    pass


def leerRegistro(dict):
  print('Su base de datos contiene los siguientes registros: ')
  for key,value in dict.items():
   print(f'{key} : {value}')

def login(dict):
  usuario = input(str('ingrese su nombre de usuario: '))
  while True:
    if usuario not in dict.keys():
      print('El usuario no existe')
      usuario = input(str('ingrese su nombre de usuario: '))
    else:
      break
  contraseña = input('Ingrese su contraseña: ')
  contador=1
  while True:
    if contador == 3:
      print('No le quedan mas intentos, vuleva a intentarlo mas tarde...')
      break
    elif contraseña not in dict.values():
      print('Contraseña incorrecta')
      contador += 1
      contraseña = input('Ingrese su contraseña: ')
    else:
      print('Se inicio sesion correctamente')
      break

def guardarTxt(dict):
  archivo_base =open('C:/Users/mauro/Proyecto Coder/Archivos/archivo_base.txt','w')
  for key,value in dict.items():
    archivo_base.write(f'{key} : {value}\n')

  archivo_base.close()
  print('Su Base de datos ha sido guardada correctamente')

def guardarJson(dict):
  mi_file_Json =open('C:/Users/mauro/Proyecto Coder/Archivos/archivo_base.json','w')
  json.dump(BD,mi_file_Json,indent=2)
  mi_file_Json.close()
  print('Su Base de datos ha sido guardada correctamente')


Registro(BD)
leerRegistro(BD)
guardarTxt(BD)
guardarJson(BD)



