class Platos:
    def __init__(self, cantidadDeAzucar, esBonito):
        self.cantidadDeAzucar = cantidadDeAzucar
        self.esBonito = esBonito
        
    def calcularCalorias(self, tipo):
        return tipo.calcularCalorias(self)
    
class Entradas():
    cantidadDeAzucar = 60
    esBonito = True
    
    def calcularCalorias(self, plato):
        return 3 * plato.cantidadDeAzucar + 100

class Principales():
    cantidadDeAzucar = 0
    esBonito = False
    
    def calcularCalorias(self, plato):
        return 3 * plato.cantidadDeAzucar + 100
    
class Postres:
    cantidadDeAzucar = 100
    esBonito = True
    
    cantidadColores =  3
    def calcularCalorias(self, plato):
        return 3 * plato.cantidadDeAzucar + 100
    

      
    
    