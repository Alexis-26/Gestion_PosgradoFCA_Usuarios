from .model import MYSQLDB
from datetime import datetime
import pytz
import reflex as rx

tz_bc = pytz.timezone("America/Tijuana")

class ConsultaHorarios(rx.State):
    _db:MYSQLDB = MYSQLDB()
    lista_horarios: list[tuple] = []
    horas: list[str] = ["07:00", "08:00", "09:00", "10:00", "11:00",
                        "12:00", "13:00", "14:00", "15:00", "16:00",
                        "17:00", "18:00", "19:00", "20:00", "21:00",
                        ]
    grupos: list[str] = ["700", "710", "720", "721", "730", "731", 
                         "740", "741", "750", "751", "760", "761"]
    
    horario_dict_1: dict[str, list[tuple]] = {
    "07:00": [(), (), (), (), (), ()], "08:00": [(), (), (), (), (), ()], "09:00": [(), (), (), (), (), ()], "10:00": [(), (), (), (), (), ()],
    "11:00": [(), (), (), (), (), ()], "12:00": [(), (), (), (), (), ()], "13:00": [(), (), (), (), (), ()], "14:00": [(), (), (), (), (), ()],
    "15:00": [(), (), (), (), (), ()], "16:00": [(), (), (), (), (), ()], "17:00": [(), (), (), (), (), ()], "18:00": [(), (), (), (), (), ()],
    "19:00": [(), (), (), (), (), ()], "20:00": [(), (), (), (), (), ()], "21:00": [(), (), (), (), (), ()],
    }
    horario_dict_2: dict[str, list[tuple]] = {
    "07:00": [(), (), (), (), (), ()], "08:00": [(), (), (), (), (), ()], "09:00": [(), (), (), (), (), ()], "10:00": [(), (), (), (), (), ()],
    "11:00": [(), (), (), (), (), ()], "12:00": [(), (), (), (), (), ()], "13:00": [(), (), (), (), (), ()], "14:00": [(), (), (), (), (), ()],
    "15:00": [(), (), (), (), (), ()], "16:00": [(), (), (), (), (), ()], "17:00": [(), (), (), (), (), ()], "18:00": [(), (), (), (), (), ()],
    "19:00": [(), (), (), (), (), ()], "20:00": [(), (), (), (), (), ()], "21:00": [(), (), (), (), (), ()],
    }
    
    salones_informacion: dict[str, bool] = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False,}
    salones_primer_nivel: list[str] = ["A", "B", "101", "102", "103", "104", ]
    salones_segundo_nivel: list[str] = ["C", "D", "201", "202", "203", "204"]

    select_horas:str = ""
    fecha_seleccionada:str = ""
    grupo = ""

    min_date: str = datetime.today().strftime("%Y-%m-%d")


    @rx.var
    def fecha_hoy(self) -> str:
        return datetime.now(tz_bc).strftime("%Y-%m-%d")

    @rx.var
    def fecha_hoy_formato(self) -> str:
        return datetime.now(tz_bc).strftime("%d-%m-%Y")

    @rx.var
    def hora_actual(self) -> str:
        return f"{datetime.now(tz_bc).hour:02d}:00"
    
    def filter_fecha(self, fecha:str):
        self.lista_horarios = []
        self.fecha_seleccionada = fecha
        self.salones_informacion = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False, }
        self.informacion_horarios()

    def filter_hora(self, hora:str):
        self.select_horas = hora
        self.salones_informacion = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False,}
        self.informacion_horarios()

    def filter_grupo(self, grupo:str):
        self.grupo = grupo
        self.informacion_horarios()

    def convertir_a_hora_str(self, td):
        horas = td.seconds // 3600
        minutos = (td.seconds % 3600) // 60
        return f"{horas:02d}:{minutos:02d}"
    
    def informacion_horarios(self):
        if self.fecha_seleccionada == "" and self.select_horas == "":
            self.fecha_seleccionada = self.fecha_hoy
            self.select_horas = self.hora_actual

        resultado = self._db.consulta_asignacion_fecha(self.fecha_seleccionada)
        self.horario_dict_1 = {
            "07:00": [(), (), (), (), (), ()], "08:00": [(), (), (), (), (), ()], "09:00": [(), (), (), (), (), ()], "10:00": [(), (), (), (), (), ()],
            "11:00": [(), (), (), (), (), ()], "12:00": [(), (), (), (), (), ()], "13:00": [(), (), (), (), (), ()], "14:00": [(), (), (), (), (), ()],
            "15:00": [(), (), (), (), (), ()], "16:00": [(), (), (), (), (), ()], "17:00": [(), (), (), (), (), ()], "18:00": [(), (), (), (), (), ()],
            "19:00": [(), (), (), (), (), ()], "20:00": [(), (), (), (), (), ()], "21:00": [(), (), (), (), (), ()],
            }
        self.horario_dict_2 = {
            "07:00": [(), (), (), (), (), ()], "08:00": [(), (), (), (), (), ()], "09:00": [(), (), (), (), (), ()], "10:00": [(), (), (), (), (), ()],
            "11:00": [(), (), (), (), (), ()], "12:00": [(), (), (), (), (), ()], "13:00": [(), (), (), (), (), ()], "14:00": [(), (), (), (), (), ()],
            "15:00": [(), (), (), (), (), ()], "16:00": [(), (), (), (), (), ()], "17:00": [(), (), (), (), (), ()], "18:00": [(), (), (), (), (), ()],
            "19:00": [(), (), (), (), (), ()], "20:00": [(), (), (), (), (), ()], "21:00": [(), (), (), (), (), ()],
            }
                        
        if resultado:
            self.lista_horarios = []
            
            if self.select_horas or self.fecha_seleccionada:
                res = [tuple(row) for row in resultado]
                
                # Procesar cada tupla y modificar el nombre
                horarios_procesados = []
                for r in res:
                    lista_r = list(r)  # Convertir la tupla a lista para modificar

                    nombres = r[1].split()  # Dividir el nombre completo
                    if len(nombres) >= 2:
                        lista_r[1] = f"{nombres[0]} {nombres[1]}"  # Modificar solo el nombre
                    
                    hora_validar = self.convertir_a_hora_str(lista_r[6])

                    
                    if r[0] in self.salones_primer_nivel:
                        idx = self.salones_primer_nivel.index(r[0])
                        if hora_validar not in self.horario_dict_1:
                            self.horario_dict_1[hora_validar] = [() for _ in self.salones_primer_nivel]
                        self.horario_dict_1[hora_validar][idx] = tuple(lista_r)
                    
                    if r[0] in self.salones_segundo_nivel:
                        idx = self.salones_segundo_nivel.index(r[0])
                        if hora_validar not in self.horario_dict_2:
                            self.horario_dict_2[hora_validar] = [() for _ in self.salones_segundo_nivel]
                        self.horario_dict_2[hora_validar][idx] = tuple(lista_r)

                    # Filtrar por hora si coincide
                    if hora_validar == self.select_horas:
                        
                        #Modifica el estado
                        if r[0] in self.salones_informacion:
                            self.salones_informacion[r[0]] = True
                            
                        horarios_procesados.append(tuple(lista_r))  # Convertir de vuelta a tupla
                        
                self.lista_horarios = horarios_procesados

        if not self.lista_horarios:
            self.lista_horarios.append(tuple(["NONE"]))
