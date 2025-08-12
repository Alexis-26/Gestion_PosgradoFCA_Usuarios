from .model import MYSQLDB
import reflex as rx
from datetime import datetime

class Tabla_ConsultaHorarios(rx.State):
    _db:MYSQLDB = MYSQLDB()
    lista_horarios: list[tuple] = []
    horas: list[str] = ["07:00", "08:00", "09:00", "10:00", "11:00",
                        "12:00", "13:00", "14:00", "15:00", "16:00",
                        "17:00", "18:00", "19:00", "20:00", "21:00",
                        "22:00"]
    grupos: list[str] = ["700", "710", "720", "721", "730", "731", 
                         "740", "741", "750", "751", "760", "761"]
    #salones_primer_nivel: list[str] = ["101", "102", "103", "104", "A", "B"]
    #salones_segundo_nivel: list[str] = ["201", "202", "203", "204", "C", "D"]
    #lista_informacion_reserva: list[str] = []
    # mostrar_formulario:bool = False
    # checkbox_hrs:dict[str, list[bool, bool]] = {"7:00":[False, False], "8:00":[False, False], "9:00":[False, False], "10:00":[False, False], "11:00":[False, False],
    #                 "12:00": [False, False], "13:00":[False, False], "14:00":[False, False], "15:00": [False, False], "16:00":[False, False], "17:00": [False, False],
    #                 "18:00": [False, False], "19:00":[False, False], "20:00":[False, False], "21:00":[False, False], "22:00":[False, False]}
    # select_horario:bool = True
    # menu:bool = False
    select_horas:str = f"{datetime.now().hour:02d}:00"
    fecha_seleccionada:str = datetime.now().strftime("%Y-%m-%d")
    grupo = ""
    # fecha_fin_habilitado:bool = True
    # hora_fijo_checked:bool = False
    
    def filter_fecha(self, fecha:str):
        self.fecha_seleccionada = fecha
        print(fecha)
        self.informacion_horarios()

    def filter_hora(self, hora:str):
        self.select_horas = hora
        print(hora)
        self.informacion_horarios()

    def filter_grupo(self, grupo:str):
        self.grupo = grupo
        print(grupo)
        self.informacion_horarios()

    def convertir_a_hora_str(self, td):
        horas = td.seconds // 3600
        minutos = (td.seconds % 3600) // 60
        return f"{horas:02d}:{minutos:02d}"
    
    def informacion_horarios(self):
        resultado = self._db.consulta_asignacion_fecha(self.fecha_seleccionada)
        print("PROCESANDO...")
        if resultado:
            if self.select_horas or self.fecha_seleccionada:
                res = [tuple(row) for row in resultado]
                
                # Procesar cada tupla y modificar el nombre
                horarios_procesados = []
                for r in res:
                    lista_r = list(r)  # Convertir la tupla a lista para modificar
                    nombres = r[1].split()  # Dividir el nombre completo
                    if len(nombres) >= 2:
                        lista_r[1] = f"{nombres[0]} {nombres[1]}"  # Modificar solo el nombre
                    
                    # Filtrar por hora si coincide
                    if self.convertir_a_hora_str(lista_r[6]) == self.select_horas:
                        horarios_procesados.append(tuple(lista_r))  # Convertir de vuelta a tupla
                        
                self.lista_horarios = horarios_procesados
                print("Lista horarios:", self.lista_horarios)  # Debug
                if not self.lista_horarios:
                    self.lista_horarios.append(tuple(["NONE"]))

        # print("Lista horarios:", self.lista_horarios)
        # for row in self.lista_horarios:
        #     print("Row:", row[0])
    # async def consultar_horarios(self):
    #     print("está aqui")
    #     """Realiza la consulta y actualiza el estado."""
    #     # Asumiendo que tienes una instancia de la base de datos en self._db
    #     # y que consulta_horarios acepta una fecha como parámetro
    #     resultado = self._db.consulta_asignacion_fecha(self.fecha_seleccionada)
    #     self.lista_horarios = [("{:02d}:{:02d}".format(row[6].seconds // 3600, (row[6].seconds % 3600) // 60), row[0]) for row in resultado]
    #     print("Lista horarios:", self.lista_horarios)  # Debug

    async def validacion_horas(self, dato):
        await self.lista_horarios
        #salones = ["101", "102", "103", "104", "A", "B", "201", "202", "203", "204", "C", "D"]
        for row in self.lista_horarios:
            if dato == row[0]:
                return row