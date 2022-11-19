#UAI - Programacion II - Parcial 2
#Lastra, Julian Marcos.

import json
from functools import reduce
import functools

#Punto 1
class Camion:
    patente = "AB123CD"
    litros_disponibles = 25.2
    cuidad_actual = "Balcarce"
    km_litro = 0.3
    velocidad_maxima = 90

class Chofer:
    nombre = "Mick"
    apellido = "Jagger"

#Punto 2
class Cuidad:
    nombre = "Balcarce"
    nombre1 = "MardelPlata"
    nombre2 = "SierradelosPadres"
    nombre3 = "Tandil"
    distancia1 = 100
    distancia2 = 200
    distancia3 = 300
    
    def __init__(self, nombre,nombre1,nombre2,nombre3,distancia1,distancia2,distancia3):
        self.nombre = nombre
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.nombre3 = nombre3
        self.distancia1 = distancia1
        self.distancia2 = distancia2
        self.distancia3 = distancia3

#region Defino las cuidades
#1. Balcarce
# A 70 KM de Mar del Plata
# A 85 KM de Sierra de los padres
# A 60 KM de Tandil
balcarce = Cuidad("Balcarce","Mar del Plata", "Sierra de los Padres", "Tandil", 70, 85, 60)

#2. Mar Del Plata
# A 70 KM de Balcarce
# A 85 KM de Sierra de los padres
# A 60 KM de Tandil
mardel = Cuidad("Mar del Plata","Balcarce", "Sierra de los Padres", "Tandil", 70, 105, 50)

#3. Sierra de los Padres
# A 70 KM de Mar del Plata
# A 85 KM de Balcarce
# A 60 KM de Tandil
sierra = Cuidad("Sierra de los Padres","Mar del Plata", "Balcarce", "Tandil", 105, 85, 150)

#4. Tandil
# A 70 KM de Mar del Plata
# A 85 KM de Sierra de los padres
# A 60 KM de Balcarce
tandil = Cuidad("Tandil","Mar del Plata", "Sierra de los Padres", "Balcarce", 50, 150, 60)
#endregion 

#Punto 3

def estimar_viaje(camion,cuidades,recorridoTotalKM,enoughFuel,tiempoTotal):
    try:
        totalKM = []

        print("Estimando viaje...")
        #Calculo de los KM totales a recorrer
        cuidadActual = camion.cuidad_actual
        for cuidad in cuidades:
            if cuidad.nombre == cuidadActual:
                print(f"El camion inicia su recorrido desde {camion.cuidad_actual}")
                cuidadActual = camion.cuidad_actual
            elif cuidadActual == cuidad.nombre1:
                recorridoTotalKM = recorridoTotalKM + cuidad.distancia1
                cuidadActual = cuidad.nombre
                totalKM.append(cuidad.distancia1)
            elif cuidadActual == cuidad.nombre2:
                recorridoTotalKM = recorridoTotalKM + cuidad.distancia2
                cuidadActual = cuidad.nombre
                totalKM.append(cuidad.distancia2)
            elif cuidadActual == cuidad.nombre3:
                recorridoTotalKM = recorridoTotalKM + cuidad.distancia3
                cuidadActual = cuidad.nombre
                totalKM.append(cuidad.distancia3)

        print(f"El camion va a recorrer {recorridoTotalKM} KM")

        #Calculo si el combustible va a ser suficiente para el recorrido
        if camion.litros_disponibles < (camion.km_litro*recorridoTotalKM):
            print("No alcanza la nafta para completar el recorrido")
        else:
            print("La nafta es suficiente para completar el recorrido")
            enoughFuel = True

        #Calculo el tiempo total
        tiempoTotal = (((len(cuidades)-1)* 60) + ((recorridoTotalKM/camion.velocidad_maxima)*60))
        print(f"El recorrido durara {tiempoTotal} minutos")

        estimacion = Estimacion(recorridoTotalKM,enoughFuel,tiempoTotal)

        logData(buildLaEntry(estimacion,camion))

        #Calculo el total de KM recorridos utilizando la lista totalKM y un reduce.
        
        # using reduce to compute sum of list
        print("La suma de los elemntos de KM recorridos es : ", end="")
        #EXPRESION LAMBDA Y REDUCE
        print(functools.reduce(lambda a, b: a+b, totalKM))

        return estimacion

    except Exception as e:
        print("Se encontro un error al procesar los datos del viaje.")
        print(e)


#Punto 4
class Estimacion:
    recorridoTotal = 10
    naftaSuficiente = False
    tiempoTotal = 60
    patente = "AB123CD"

    def __init__(self, recorrido,nafta,tiempo):
        self.recorridoTotal = recorrido
        self.naftaSuficiente = nafta
        self.tiempoTotal = tiempo

def buildLaEntry(estimacion,camion):
    entry = {
        "recorridoTotal":estimacion.recorridoTotal,
        "naftaSuficiente":str(estimacion.naftaSuficiente),
        "tiempoTotal":estimacion.tiempoTotal,
        "patente":camion.patente
    }
    return entry

def logData(entry):
    try:
        print("Guardando datos..")
        #Guardo la estimacion y la patente del camion.

        fullJson = LoadData()
        fullJson.append(entry)

        json_objectW = json.dumps(fullJson, indent=4)
        
        with open("datos.json", "w") as outfile:
            outfile.write(json_objectW)
    except Exception as e:
        print("Error en la escritura de informacion")
        print(e)

#Punto 5. 
def LoadData():
    try:
        print("Leyendo archivo...")

        with open('datos.json', 'r') as openfile:
            json_objectR = json.load(openfile)

        listaEstimaciones = []

        for estimacion in json_objectR:
            #map filter o reduce de las que superaron los 1000KM.
            #map filter o reduce de las que son de x patente.
            #print("Realizando el calculo...")
            listaEstimaciones.append(estimacion)

        return listaEstimaciones
    except Exception as e:
        print("Error al leer el archivo")
        print(e)

def main():
    try:
        print("######################################################")
        print("############ PROGRAMACION II - PARCIAL ###############")
        print("######################################################")

        recorridoTotalKM = 0
        tiempoTotal = 0
        enoughFuel = False 

        recorridos = []
        #Por defecto hay 4 destinos posibles balcarce, mardel, sierra y tandil
        #Podemos agregar la cantidad que se quiera a la lista de recorridos, mientras sea uno de los mencionados
        recorridos.append(balcarce) 
        recorridos.append(mardel)
        recorridos.append(sierra)
        recorridos.append(tandil)
        recorridos.append(mardel)
        recorridos.append(balcarce) 
        recorridos.append(mardel)

        camion1 = Camion
        estimar_viaje(camion1,recorridos,recorridoTotalKM,enoughFuel,tiempoTotal)

        lista = LoadData()
        listaPatente = []
        listaMayor = []
        listaMenor = []

        for item in lista:
            if item['patente'] == "AB123CD":
                listaPatente.append(item)
        
        print("Recorridos mayores a 1000 KM: ")
        for item in listaPatente:
            if item['recorridoTotal'] > 1000:
                listaMayor.append(item)
                print(item)

        print("Recorridos menores a 1000 KM: ")
        for item in listaPatente:
            if item['recorridoTotal'] < 1000:
                listaMenor.append(item)
                print(item)



    except Exception as e:
        print("Error en el modulo princial del programa")
        print(e)
      
main()