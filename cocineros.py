from platos import  *

class Cocineros:
    def __init__(self, especialidad):
        self.especialidad = especialidad
    
    def catarPlato(self, tipo):
        return tipo.catarPlato(self)
        
    def cambiarEspecialidad(self, tipo):
        return tipo.cambiarEspecialidad(self)
    
    def cocinar(self, tipo):
        return tipo.cocinar(self)
    
class CookStyles:
    def allStyles(self, dato):
        cocinero = Cocineros(dato)
        return cocinero.especialidad

class Pasteleros(CookStyles):
    nivelDeDulzor = 30
    
    def catarPlato(self, plato):
        return round(5 * plato.cantidadDeAzucar / self.nivelDeDulzor,2)
    
    def cambiarEspecialidad(self):
        return self.allStyles("chef")
    
    def cocinar(self):
        return Postres()
    
class Chefs(CookStyles):
    limiteCalorias = 10
    
    def catarPlato(self, plato):
        calorias = plato.cantidadDeAzucar * 3 / 100
        if plato.esBonito and  calorias < self.limiteCalorias:
            return 10
        
        else:
            return 0
    
    def cambiarEspecialidad(self):
        return self.allStyles("pastelero")
    
    def cocinar(self):
        return Principales()
    
class Souschef(Chefs):
    def catarPlato(self, plato):
        calorias = plato.cantidadDeAzucar * 3 / 100
        if plato.esBonito and  calorias < self.limiteCalorias:
            return 10
        
        else:
            return calorias / 100
        
    def cocinar(self):
        return Entradas()


