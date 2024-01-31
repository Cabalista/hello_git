import time 

class Usuarios:
  def __init__(self, nombre, apellidos, edad):
    self.nombre = nombre
    self.apellidos = apellidos
    self.edad = edad

  def setNombre(self, nombre):
    self.nombre = nombre

  def getNombre(self):
    print(self.nombre)
  
