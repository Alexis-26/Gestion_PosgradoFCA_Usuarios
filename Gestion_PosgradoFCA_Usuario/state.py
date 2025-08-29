from .model import MYSQLDB
import reflex as rx
from datetime import datetime
import pytz

tz_bc = pytz.timezone("America/Tijuana")

class ConsultaHorarios(rx.State):
    _db:MYSQLDB = MYSQLDB()
    lista_horarios: list[tuple] = []
    horas: list[str] = ["07:00", "08:00", "09:00", "10:00", "11:00",
                        "12:00", "13:00", "14:00", "15:00", "16:00",
                        "17:00", "18:00", "19:00", "20:00", "21:00",
                        "22:00"]
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
    #lista_informacion_reserva: list[str] = []
    # mostrar_formulario:bool = False
    # checkbox_hrs:dict[str, list[bool, bool]] = {"7:00":[False, False], "8:00":[False, False], "9:00":[False, False], "10:00":[False, False], "11:00":[False, False],
    #                 "12:00": [False, False], "13:00":[False, False], "14:00":[False, False], "15:00": [False, False], "16:00":[False, False], "17:00": [False, False],
    #                 "18:00": [False, False], "19:00":[False, False], "20:00":[False, False], "21:00":[False, False], "22:00":[False, False]}
    # select_horario:bool = True
    # menu:bool = False
    select_horas:str = ""
    fecha_seleccionada:str = ""
    grupo = ""
    #fecha_actual = datetime.today().strftime("%d-%m-%Y")
    # fecha_fin_habilitado:bool = True
    # hora_fijo_checked:bool = False

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
        print(fecha)
        self.salones_informacion = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False, }
        self.informacion_horarios()

    def filter_hora(self, hora:str):
        self.select_horas = hora
        print(hora)
        self.salones_informacion = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False,}
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
        if self.fecha_seleccionada == "" and self.select_horas == "":
            self.fecha_seleccionada = self.fecha_hoy
            self.select_horas = self.hora_actual

        print(self.select_horas)
        resultado = self._db.consulta_asignacion_fecha(self.fecha_seleccionada)
        print("PROCESANDO...")  
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

                            # if r[0] in self.salones_segundo_nivel:
                            #     self.horario_dict_2[hora_validar] = tuple(lista_r)
                            
                        horarios_procesados.append(tuple(lista_r))  # Convertir de vuelta a tupla
                        
                self.lista_horarios = horarios_procesados
                print("Lista horarios:", self.lista_horarios)  # Debug
                print("Cambio estado: ", self.salones_informacion) # Debug
                print("Diccionario listo 1: ", self.horario_dict_1)
                print("Diccionario listo 2: ", self.horario_dict_2)
        if not self.lista_horarios:
            self.lista_horarios.append(tuple(["NONE"]))

    async def validacion_horas(self, dato):
        await self.lista_horarios
        #salones = ["101", "102", "103", "104", "A", "B", "201", "202", "203", "204", "C", "D"]
        for row in self.lista_horarios:
            if dato == row[0]:
                return row

# class Tabla_ConsultaHorarios(rx.State):
#     _db:MYSQLDB = MYSQLDB()
#     lista_horarios: list[tuple] = []
#     lista_informacion_reserva: list[str] = []
#     mostrar_formulario:bool = False
#     checkbox_hrs:dict[str, list[bool, bool]] = {"7:00":[False, False], "8:00":[False, False], "9:00":[False, False], "10:00":[False, False], "11:00":[False, False],
#                     "12:00": [False, False], "13:00":[False, False], "14:00":[False, False], "15:00": [False, False], "16:00":[False, False], "17:00": [False, False],
#                     "18:00": [False, False], "19:00":[False, False], "20:00":[False, False], "21:00":[False, False], "22:00":[False, False]}
#     select_horario:bool = True
#     menu:bool = False
#     fecha_seleccionada:str = ""
#     fecha_fin_habilitado:bool = True
#     hora_fijo_checked:bool = False
#     no_empleado = ""
#     fecha_actual = datetime.today().strftime("%d-%m-%Y")

#     async def informacion_horarios(self):
#         self.lista_horarios = [] # Reinicia la lista
#         #self.no_empleado = await self.get_var_value(Login.no_empleado_activo)
#         resultado = self._db.consulta_horarios(self.no_empleado)
#         # Convierte el resultado en una lista de tuplas
#         self.lista_horarios = [tuple(row) for row in resultado]
#         print(self.lista_horarios)

#     def actualizar_horarios(self):
#         self.lista_horarios = [] # Reinicia la lista
#         resultado = self._db.consulta_horarios(self.no_empleado)
#         # Convierte el resultado en una lista de tuplas
#         self.lista_horarios = [tuple(row) for row in resultado]
#         print(self.lista_horarios)

#     def eliminar_reserva(self, salon:str, fecha:str, hora:str):
#         query = self._db.eliminar_reserva(salon, fecha, hora)
#         print(salon, fecha, hora)
#         print("Eliminado correctamente...")
#         self.actualizar_horarios()

#     def carga_editar_reserva(self, salon: str, no_empleado: str, docente: str, cve_materia:str, curso_materia: str, grupo: str, fecha_inicio: str, fecha_fin: str, hora: str, status: str):
#         """Cargando datos para editar la reserva"""

#         hora_modificada = hora.split(":")[0] + ":" + hora.split(":")[1]
#         hora_modificada = hora_modificada.lstrip("0")

#         if status == "FIJO":
#             self.hora_fijo_checked = True
#             self.fecha_fin_habilitado = False

#         # Guardar la información en la lista de reserva
#         self.lista_informacion_reserva = [salon, no_empleado, docente, cve_materia, curso_materia, grupo, fecha_inicio, fecha_fin, hora_modificada, status]

#         # Mostrar formulario
#         print("Cargando información...")
#         print("Listo...")
#         self.mostrar_formulario = True

#     def component_menu_horas(self, value):
#         self.menu = value

#     # Esta funcion es para filtrar los horarios disponibles en el salon seleccionado con la fecha seleccionada en el formulario
#     def filtro_horarios(self, salon:str, fecha:str):
#         if salon and fecha:
#             lista_registros = []
#             self.checkbox_hrs:dict[str, list[bool, bool]] = {"7:00":[False, False], "8:00":[False, False], "9:00":[False, False], "10:00":[False, False], "11:00":[False, False],
#                     "12:00": [False, False], "13:00":[False, False], "14:00":[False, False], "15:00": [False, False], "16:00":[False, False], "17:00": [False, False],
#                     "18:00": [False, False], "19:00":[False, False], "20:00":[False, False], "21:00":[False, False], "22:00":[False, False]}
#             # NOTA PREGUNTAR CON JUAN QUE PASA CON LA CONSULTA YA QUE LA CONSULTA TRAE TODOS LOS DATOS DE LA TABLA 
#             resultados = self._db.consulta_horarios_ocupados(salon, fecha)
#             # Convierte el resultado en una lista de tuplas
#             for row in resultados:
#                 hora = (datetime.datetime.min + row[6]).strftime("%H:%M")  # Formato HH:MM
#                 hora = hora.lstrip("0") if hora.startswith("0") else hora  # Elimina el cero solo si está al inicio
#                 lista_registros.append(hora)

#             for key, value in self.checkbox_hrs.items():
#                 for i in lista_registros:
#                     if i == key:
#                         self.checkbox_hrs[key][1] = True

#             #print(self.checkbox_hrs)
#             print(lista_registros)
#             lista_registros = []  

#     # Esta funcion habilita el select de horarios cuando existe una fecha seleccionada en el input del formulario
#     def toggle_select_horas(self, fecha):
#         self.fecha_seleccionada = fecha
#         self.filtro_horarios(self.lista_informacion_reserva[0], fecha)
#         self.select_horario = False

#     def hrs_seleccionadas(self, value, hora):
#         # Cambia el estado del checkbox de la hora seleccionada para mantener el estado en el formulario
#         self.checkbox_hrs[hora][0] = value

#     def toggle_fecha_fin(self):
#         self.fecha_fin_habilitado = not self.fecha_fin_habilitado
#         self.hora_fijo_checked = not self.hora_fijo_checked

#     def cancelar(self):
#         self.mostrar_formulario = False
#         self.menu = False
#         self.fecha_fin_habilitado= True
#         self.select_horario = True
#         self.hora_fijo_checked = False
#         self.checkbox_hrs:dict[str, list[bool, bool]] = {"7:00":[False, False], "8:00":[False, False], "9:00":[False, False], "10:00":[False, False], "11:00":[False, False],
#                     "12:00": [False, False], "13:00":[False, False], "14:00":[False, False], "15:00": [False, False], "16:00":[False, False], "17:00": [False, False],
#                     "18:00": [False, False], "19:00":[False, False], "20:00":[False, False], "21:00":[False, False], "22:00":[False, False]}

#     def actualizar_reserva(self, form_data:dict):
#         # DATOS CARGADOS PARA ACTUALIZAR
#         salon = self.lista_informacion_reserva[0]
#         no_empleado = self.lista_informacion_reserva[1]
#         clave_materia = self.lista_informacion_reserva[3]
#         grupo = self.lista_informacion_reserva[5]
#         fecha_inicio = self.lista_informacion_reserva[6]
#         fecha_fin = self.lista_informacion_reserva[7]
#         hora = self.lista_informacion_reserva[8]
        
#         #DATOS A ACTUALIZAR
#         no_empleado_nuevo = form_data.get("numero_empleado")
#         nombre_docente = form_data.get("nombre_maestro")
#         clave_materia_nuevo = form_data.get("clave_materia")
#         nombre_materia = form_data.get("nombre_materia")
#         grupo_nuevo = form_data.get("grupo")
#         h_fijo = form_data.get("horario_fijo")
#         fecha_inicio_nuevo = form_data.get("fecha_inicio")
#         fecha_fin_nuevo = form_data.get("fecha_fin")


#         # Sección de horas reservadas
#         # Nota: Es el unico que no se extrae del formulario ya que el componente es creado, no de reflex
#         horas_reservadas = []
#         for key, value in self.checkbox_hrs.items():
#             if value[0]: # [0] es el valor booleano del checkbox para saber si esta seleccionado
#                 # print(key, value[0])
#                 horas_reservadas.append(key)
        
#         hora_nuevo = horas_reservadas[0] if len(horas_reservadas) > 0 else hora # Solo se puede seleccionar una hora en caso de que no se utiliza la que fue cargada

#         if h_fijo == "fijo":
#             for hora in horas_reservadas:
#                 #query = self._db.add_reserva(clave_salon=salon, no_empleado=no_empleado, clave_materia=clave_materia, grupo=grupo, 
#                                             #fecha_inicio=fecha_inicio, fecha_final=fecha_fin, hora=hora, status="FIJO")
#                 query = self._db.update_reserva(salon, no_empleado, clave_materia, grupo, fecha_inicio, fecha_fin, hora, salon, no_empleado_nuevo, clave_materia_nuevo, grupo_nuevo, fecha_inicio_nuevo, fecha_fin_nuevo, hora_nuevo, status_nuevo="FIJO")
#                 print("SE HA ACTUALIZADO UNA RESERVA FIJA")
#         else:
#             for hora in horas_reservadas:
#                 #query = self._db.add_reserva(salon, no_empleado, clave_materia, grupo, fecha_inicio, None, hora, status="RESERVADO")
#                 query = self._db.update_reserva(salon, no_empleado, clave_materia, grupo, fecha_inicio, fecha_fin, hora, salon, no_empleado_nuevo, clave_materia_nuevo, grupo_nuevo, fecha_inicio_nuevo, fecha_fin_nuevo, hora_nuevo, status_nuevo="RESERVADO")
#                 print("SE HA ACTUALIZADO UNA RESERVA")
        
#         self.mostrar_formulario = False
#         self.informacion_horarios()
        # NOTA EL PROCEDURE DE JUAN DE ACTUALIZAR ASIGNACION NO ESTA FUNCIONANDO CORRECTAMENTE
        # FALTA TAMBIEN VALIDAR QUE EL SELECT SOLO DEBA DE SER UNA HORA PARA EL CAMBIO DE HORA


# class Tabla_ConsultaHorarios(rx.State):
#     _db:MYSQLDB = MYSQLDB()
#     lista_horarios: list[tuple] = []
#     horas: list[str] = ["07:00", "08:00", "09:00", "10:00", "11:00",
#                         "12:00", "13:00", "14:00", "15:00", "16:00",
#                         "17:00", "18:00", "19:00", "20:00", "21:00",
#                         "22:00"]
#     grupos: list[str] = ["700", "710", "720", "721", "730", "731", 
#                          "740", "741", "750", "751", "760", "761"]
#     #salones_primer_nivel: list[str] = ["101", "102", "103", "104", "A", "B"]
#     #salones_segundo_nivel: list[str] = ["201", "202", "203", "204", "C", "D"]
#     #lista_informacion_reserva: list[str] = []
#     # mostrar_formulario:bool = False
#     # checkbox_hrs:dict[str, list[bool, bool]] = {"7:00":[False, False], "8:00":[False, False], "9:00":[False, False], "10:00":[False, False], "11:00":[False, False],
#     #                 "12:00": [False, False], "13:00":[False, False], "14:00":[False, False], "15:00": [False, False], "16:00":[False, False], "17:00": [False, False],
#     #                 "18:00": [False, False], "19:00":[False, False], "20:00":[False, False], "21:00":[False, False], "22:00":[False, False]}
#     # select_horario:bool = True
#     # menu:bool = False
#     select_horas:str = f"{datetime.now().hour:02d}:00"
#     fecha_seleccionada:str = datetime.now().strftime("%Y-%m-%d")
#     grupo = ""
#     # fecha_fin_habilitado:bool = True
#     # hora_fijo_checked:bool = False
    
#     def filter_fecha(self, fecha:str):
#         self.fecha_seleccionada = fecha
#         print(fecha)
#         self.informacion_horarios()

#     def filter_hora(self, hora:str):
#         self.select_horas = hora
#         print(hora)
#         self.informacion_horarios()

#     def filter_grupo(self, grupo:str):
#         self.grupo = grupo
#         print(grupo)
#         self.informacion_horarios()

#     def convertir_a_hora_str(self, td):
#         horas = td.seconds // 3600
#         minutos = (td.seconds % 3600) // 60
#         return f"{horas:02d}:{minutos:02d}"
    
#     def informacion_horarios(self):
#         resultado = self._db.consulta_asignacion_fecha(self.fecha_seleccionada)
#         print("PROCESANDO...")
#         if resultado:
#             if self.select_horas or self.fecha_seleccionada:
#                 res = [tuple(row) for row in resultado]
                
#                 # Procesar cada tupla y modificar el nombre
#                 horarios_procesados = []
#                 for r in res:
#                     lista_r = list(r)  # Convertir la tupla a lista para modificar
#                     nombres = r[1].split()  # Dividir el nombre completo
#                     if len(nombres) >= 2:
#                         lista_r[1] = f"{nombres[0]} {nombres[1]}"  # Modificar solo el nombre
                    
#                     # Filtrar por hora si coincide
#                     if self.convertir_a_hora_str(lista_r[6]) == self.select_horas:
#                         horarios_procesados.append(tuple(lista_r))  # Convertir de vuelta a tupla
                        
#                 self.lista_horarios = horarios_procesados
#                 print("Lista horarios:", self.lista_horarios)  # Debug
#                 if not self.lista_horarios:
#                     self.lista_horarios.append(tuple(["NONE"]))

#         # print("Lista horarios:", self.lista_horarios)
#         # for row in self.lista_horarios:
#         #     print("Row:", row[0])
#     # async def consultar_horarios(self):
#     #     print("está aqui")
#     #     """Realiza la consulta y actualiza el estado."""
#     #     # Asumiendo que tienes una instancia de la base de datos en self._db
#     #     # y que consulta_horarios acepta una fecha como parámetro
#     #     resultado = self._db.consulta_asignacion_fecha(self.fecha_seleccionada)
#     #     self.lista_horarios = [("{:02d}:{:02d}".format(row[6].seconds // 3600, (row[6].seconds % 3600) // 60), row[0]) for row in resultado]
#     #     print("Lista horarios:", self.lista_horarios)  # Debug

#     async def validacion_horas(self, dato):
#         await self.lista_horarios
#         #salones = ["101", "102", "103", "104", "A", "B", "201", "202", "203", "204", "C", "D"]
#         for row in self.lista_horarios:
#             if dato == row[0]:
#                 return row