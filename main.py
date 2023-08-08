from proyecto_paquetes_coder.Segunda_Entrega import*

persona1=Persona('Ana','Limbo',123123,34)
empresa1 = Empresa('Havvana','20-345-1','Av.Peralta Ramos 234','Factura A')
cliente_persona=Cliente('mauro@gmail.com','efectivo','Mauro','Albe',123456,35)
cliente_empresa=Cliente('loschurros@gfmail.com','cheque',razon_social='Loschuroos S.R.L',cuit='23-2456-4',tipoFactura='"A"')

print(persona1.saludar())
print(persona1)
print(empresa1.pedirCotizacion('apple','Iphone13',1000))
print(cliente_persona.saludar())
print(cliente_persona)
print(cliente_persona.comprar('Laptop','AppleStore'))

print(cliente_empresa.comprar('Iphone 15','AppleStore',True))
