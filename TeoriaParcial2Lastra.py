#Punto 2. Funcion de orden superior
def alquilarAuto(auto):
    def alquilar_bwm():
        print("Alquilo un BMW")
    def alquilar_audi():
        print("Alquilo un Audi")
    alquilar_func = { 
        "bmw" : alquilar_bwm,
        "audi" : alquilar_audi
    }
    return alquilar_func[auto]
alquilarAuto("bmw")()

#Punto 4. Funcion Lambda
def mutiplicador(n):
  return lambda a : a * n
cantidadMults = mutiplicador(3)
print(cantidadMults(222))
#>>666

#Punto 5. Comprension de listas.
autos = ["bmw", "audi", "ford", "Lamorbigini", "Paganni"]
listaSinAudis = [x for x in autos if x != "audi"]

#Punto 7. 
from Saludo import Saludar
Saludar()
#>> "Buenos dias"

#Punto 9. Expresiones regulares

import re
txt = "51234@uai.edu.ar"
x = re.findall("[0-9]+@uai.edu.ar\Z", txt)
print(x)

