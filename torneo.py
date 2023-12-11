from cocineros import *
from platos import *

class Torneo:
    catadores = []

    def participar(self, cocinero):
        plato = cocinero.cocinar()
        calificacion = cocinero.catarPlato(plato)
        self.catadores.append(calificacion)

    def encontrarGanador(self):
        if not self.catadores:
            return None  # No se puede establecer un ganador si no hay catadores
        ganador = self.catadores.index(max(self.catadores))
        return ganador
       
# Creo los objetos

#Platos

plato_1 = Platos(60, True)
plato_2 = Platos(0, False)
plato_3 = Platos(100, True)

#Cocineros

pastelero_1 = Pasteleros()
chef_1 = Chefs()

#Torneo

torneo = Torneo()

#Impresion de resultados

#Imprimimos el calculo de las calorias

print()
print("********************************************************************************************************")
print("*************************************** Cantidad de calorias *******************************************")
print("********************************************************************************************************")
print()
print(f"La cantidad de calorias del plato 1 son {Entradas().calcularCalorias(plato_1)}")
print(f"La cantidad de calorias del plato 2 son {Principales().calcularCalorias(plato_2)}")
print(f"La cantidad de calorias del plato 3 son {Postres().calcularCalorias(plato_3)}")
print()

# Catamos los platos

print()
print("********************************************************************************************************")
print("*****************************************  Califacion platos *******************************************")
print("********************************************************************************************************")
print()
print(f"La calificacion del plato 1 fue hecha por un pastelero y es de {pastelero_1.catarPlato(plato_1)}")
print(f"La calificacion del plato 2 fue hecha por un chef y es de {chef_1.catarPlato(plato_2)}")
print(f"La calificacion del plato 3 fue hecha por un chef y es de {chef_1.catarPlato(plato_3)}")
print()

#Cambiamos la especialidad

print()
print("********************************************************************************************************")
print("***************************************  Cambiar especialidad ******************************************")
print("********************************************************************************************************")
print()

print(f"La especialidad del pastelero cambió a {Pasteleros.cambiarEspecialidad(chef_1)}")
print(f"La especialidad del chef cambió a {Chefs.cambiarEspecialidad(pastelero_1)}")
print()

#Creando especialidad souschef

print()
print("********************************************************************************************************")
print("*************************************  Crear especialidad souschef *************************************")
print("********************************************************************************************************")
print()

souschef_1 = Souschef()
souschef_1.limiteCalorias = 2
print(f"La calificacion del plato 3 fue hecha por un souschef y es de {round(souschef_1.catarPlato(plato_3),2)}")
print(f"La especialidad del souschef cambió a {Souschef.cambiarEspecialidad(pastelero_1)}")
print()

#Creando especialidad souschef

print()
print("********************************************************************************************************")
print("******************************************  Crear un plato *********************************************")
print("********************************************************************************************************")
print()

plato_pastelero = pastelero_1.cocinar()
plato_chef = chef_1.cocinar()
plato_souschef = souschef_1.cocinar()

print(f"El pastelero ha cocinado un postre con {plato_pastelero.cantidadColores} colores y {plato_pastelero.cantidadDeAzucar}kg de azucar")
print(f"El chef ha cocinado un plato principal con {plato_chef.cantidadDeAzucar}kg de azucar")
print(f"El souschef ha cocinado una entrada con {plato_souschef.cantidadDeAzucar}kg de azucar")
print()

#Creando especialidad souschef

print()
print("********************************************************************************************************")
print("*************************************  Competir en la competencia **************************************")
print("********************************************************************************************************")
print()

torneo.participar(chef_1)
torneo.participar(pastelero_1)
torneo.participar(souschef_1)


ganador = torneo.encontrarGanador()

if ganador is not None:
    print(f"El ganador del torneo es el cocinero {ganador + 1}")
else:
    print("No se presento ningun cocinero al torneo.")

print("********************************************************************************************************")
print()