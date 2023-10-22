import pandas as pd
from funcionsumar import sumararboles

#Analizar una lista de datos
ciudades=["Medellín", "Bogotá", "Barranquilla","Leticia","Arauca", "Sincelejo","Montería","Cali"]

#Analizar una lista de diccionarios
estudiantes=[
    {"id":1,"nombre":"el juli liverpool","promedio":2.8},
    {"id":2,"nombre":"Maria del dim","promedio":2.5},
    {"id":3,"nombre":"Pipe","promedio":2.94},
    {"id":4,"nombre":"Anndy","promedio":2.7},
    {"id":5,"nombre":"Cata","promedio":2.84}
]

#Hacer dos tipos de arboles que aparezcan en los 125 municipios de antioquia
arbolesporMunicipio=[
    {"id":1, "municipio":"Carolina del principe","tipo":"guayacanes","cantidad":1500}
]

#Convirtiendo listas y listas de diccionarios en DATAFRAMES
dataframe1=pd.DataFrame(ciudades)
dataframe2=pd.DataFrame(estudiantes)
print(dataframe1)
print(dataframe2)

numeroArbolesOriente=12000000
numeroArbolesSuroeste=3000000
numeroArbolesNorte=4000000

sumatoriaorientenorte=sumararboles(numeroArbolesNorte,numeroArbolesOriente)
sumatoriasuroesteoriente=sumararboles(numeroArbolesSuroeste,numeroArbolesOriente)

#Analizar un CSV
