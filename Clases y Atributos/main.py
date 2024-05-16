# POO - Clase y Atributos

class Persona:
    nombre = ""
    apellidos = ""
    ntelefono = ""
    nID = ""
    sexo = ""

    def __init__ (self,nombrex,apellidosx,nIDx):
        self.nombre = nombrex
        self.apellidos = apellidosx
        self.nID = nIDx

    def saludar(self):
        saludo = "Hola, mi nombre es: " + self.nombre
        return saludo

class Planilla(Persona):
    salario = 15000
    moneda = "Dolares"

    def misalario(self):
        msj = "mi Salario es de: " + str(self.salario) + " " + self.moneda
        return msj

p1 = Planilla("Carlos","Parada","123456")
p2 = Persona("Julio","Parada","987654")
print(p1.saludar() + " " + p1.misalario() + "\n" + p2.saludar() ) 
