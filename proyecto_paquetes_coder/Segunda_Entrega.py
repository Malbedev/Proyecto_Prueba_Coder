class Persona():

  def __init__(self,nombre,apellido,dni,edad):
    self.__nombre=nombre
    self.__apellido=apellido
    self.__dni=dni
    self.__edad=edad


  def get_nombre(self):
    return self.__nombre

  def get_apellido(self):
    return self.__apellido

  def __str__(self):
    return f'Hola soy {self.__nombre}!!'

  def saludar(self):
    return f'Hola soy {self.__nombre} {self.__apellido} y tengo {self.__edad} años. '


class Empresa():

  def __init__(self,razon_social,cuit,direccion,tipoFactura):
    self.__razon_social=razon_social
    self.__cuit=cuit
    self.__direccion=direccion
    self.__tipoFactura=tipoFactura

  def get_razon(self):
    return self.__razon_social
  def get_cuit(self):
    return self.__cuit
  def get_tipo(self):
    return self.__tipoFactura

  def pedirCotizacion(self,tienda,producto,precio):
    return f'El producto: {producto}, cuesta {precio} dolares en {tienda}.'



class Cliente(Persona,Empresa):

  def __init__(self,email,medio_de_pago,nombre=None,apellido=None,dni=None,edad=None,razon_social=None,cuit=None ,direccion=None,tipoFactura=None):
    Persona.__init__(self,nombre,apellido,dni,edad)
    Empresa.__init__(self,razon_social,cuit,direccion,tipoFactura)
    self.__email=email
    self.__medio_de_pago= medio_de_pago

  def __str__(self):
    return f'Cliente Creado Con exito'

  def comprar(self,producto,tienda,empresa=False):
    if empresa == False:
      return f'El cliente {self.get_nombre()} {self.get_apellido()} ha adquirido un/a {producto} en {tienda} y pago en: {self.__medio_de_pago} .Se ha enviado su factura a: {self.__email}'
    else:
      return f'El cliente {self.get_razon()}, Cuit: {self.get_cuit()}, compro un lote de: {producto} y pago en: {self.__medio_de_pago},con una factura del tipo: {self.get_tipo()}.'

