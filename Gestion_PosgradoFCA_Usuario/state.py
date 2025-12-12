from .model import MYSQLDB
from datetime import datetime
import pytz
import reflex as rx

tz_bc = pytz.timezone("America/Tijuana")

class ConsultaHorarios(rx.State):
    """
    Gestiona el estado de la página de consulta de horarios.

    Este estado maneja la lógica para:
    - Conectar a la base de datos.
    - Obtener los horarios de asignación de salones.
    - Filtrar los horarios por fecha, hora y grupo.
    - Estructurar los datos para mostrarlos en una rejilla (tabla)
      y en una vista de salones ocupados.
    """

    # --- Conexión a Base de Datos ---
    _db:MYSQLDB = MYSQLDB()

    # --- Variables de Estado (Datos) ---
    lista_horarios: list[tuple] = []

    # --- Constantes para la UI (Selects y Rejilla) ---
    horas: list[str] = ["07:00", "08:00", "09:00", "10:00", "11:00",
                        "12:00", "13:00", "14:00", "15:00", "16:00",
                        "17:00", "18:00", "19:00", "20:00", "21:00",
                        ]
    grupos: list[str] = ["700", "710", "720", "721", "730", "731", 
                         "740", "741", "750", "751", "760", "761"]
    

    # --- Diccionarios para la Rejilla de Horarios ---
    # La estructura es: { "HH:MM": [ (datos_salon_1), (datos_salon_2), ... ] }
    # Cada lista interna tiene 6 tuplas, correspondiendo a los salones
    # definidos en `salones_primer_nivel` y `salones_segundo_nivel`.
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
    
    # --- Estado de Ocupación y Listas de Salones ---
    """
    Rastrea si un salón está OCUPADO (True) o LIBRE (False)
    en la `fecha_seleccionada` y `select_horas`.
    """
    salones_informacion: dict[str, bool] = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False,}
    
    """Define el orden de los salones para la matriz"""
    salones_primer_nivel: list[str] = ["A", "B", "101", "102", "103", "104"]
    salones_segundo_nivel: list[str] = ["C", "D", "201", "202", "203", "204"]

    # --- Variables de Filtro (Estado actual de la UI) ---
    select_horas:str = ""
    fecha_seleccionada:str = ""
    grupo = ""

    # --- Configuración del DatePicker ---
    """Evita que el usuario seleccione una fecha anterior a la actual."""
    min_date: str = datetime.today().strftime("%Y-%m-%d")

    # --- Variables Computadas (@rx.var) ---
    @rx.var
    def fecha_hoy(self) -> str:
        """
        Obtiene la fecha actual en formato 'YYYY-MM-DD'.
        Usado para inicializar el filtro de fecha.
        """
        return datetime.now(tz_bc).strftime("%Y-%m-%d")

    @rx.var
    def fecha_hoy_formato(self) -> str:
        """
        Obtiene la fecha actual en formato 'DD-MM-YYYY'.
        Usado para mostrar la fecha en la UI.

        Returns:
            str: La fecha actual formateada (ej: "27-10-2025").
        """
        return datetime.now(tz_bc).strftime("%d-%m-%Y")

    @rx.var
    def hora_actual(self) -> str:
        """
        Obtiene la hora actual redondeada a la hora en punto (ej: "09:00").
        Usado para inicializar el filtro de hora.
        """
        return f"{datetime.now(tz_bc).hour:02d}:00"
    
    # --- Manejadores de Eventos (Event Handlers) ---
    def filter_fecha(self, fecha:str):
        """
        Actualiza el estado cuando el usuario selecciona una nueva fecha.

        Limpia los datos anteriores y vuelve a cargar la información
        de horarios para la nueva fecha.

        Args:
            fecha (str): La nueva fecha seleccionada ("YYYY-MM-DD").
        """
        self.lista_horarios = []
        self.fecha_seleccionada = fecha
        # Resetea el estado de ocupación de salones
        self.salones_informacion = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False, }
        # Recarga los datos con la nueva fecha
        self.informacion_horarios()

    def filter_hora(self, hora:str):
        """
        Actualiza el estado cuando el usuario selecciona una nueva hora.

        Limpia el estado de ocupación y vuelve a cargar la información
        para la nueva hora.

        Args:
            hora (str): La nueva hora seleccionada ("HH:MM").
        """
        self.select_horas = hora
        self.salones_informacion = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False,}
        self.informacion_horarios()

    def filter_grupo(self, grupo:str):
        """
        Actualiza el estado cuando el usuario selecciona un grupo.

        Vuelve a cargar la información de horarios. Se asume que
        `informacion_horarios` o la consulta de BD usan `self.grupo`.

        Args:
            grupo (str): El grupo seleccionado.
        """
        self.grupo = grupo
        self.informacion_horarios()

    def convertir_a_hora_str(self, td):
        """
        Convierte un objeto timedelta (de la BD) a un string "HH:MM".

        MySQL devuelve los campos TIME como objetos `timedelta` en Python.

        Args:
            td (timedelta): El objeto de tiempo.

        Returns:
            str: El tiempo formateado como "HH:MM".
        """
        horas = td.seconds // 3600
        minutos = (td.seconds % 3600) // 60
        return f"{horas:02d}:{minutos:02d}"
    
    # --- Lógica Principal ---
    def informacion_horarios(self):
        """
        Función principal para cargar y procesar los horarios.

        1.  Establece valores por defecto si la fecha/hora están vacías (primera carga).
        2.  Consulta la base de datos con la `fecha_seleccionada`.
        3.  Resetea los diccionarios de horarios (`horario_dict_1`, `horario_dict_2`).
        4.  Procesa los resultados de la BD:
            -   Formatea el nombre del docente (corta a Nombre + Apellido).
            -   Convierte la hora de la BD (timedelta) a string "HH:MM".
            -   Puebla los diccionarios `horario_dict_1` y `horario_dict_2`
                para la rejilla general.
            -   Filtra y puebla `lista_horarios` solo con las clases
                de la `self.select_horas`.
            -   Actualiza `salones_informacion` para saber qué salones
                están ocupados en `self.select_horas`.
        5.  Asegura que `lista_horarios` tenga un valor (incluso "NONE")
            para evitar errores en la UI.
        """

        # 1. Establecer valores por defecto en la primera carga
        if self.fecha_seleccionada == "" and self.select_horas == "":
            self.fecha_seleccionada = self.fecha_hoy
            self.select_horas = self.hora_actual
        
        # 2. Consultar la base de datos
        resultado = self._db.consulta_asignacion_fecha(self.fecha_seleccionada)

        # 3. Resetear los diccionarios de la rejilla
        # Es crucial para limpiar los datos de la consulta anterior
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
        
        # 4. Procesar los resultados si la BD devolvió datos
        if resultado:
            self.lista_horarios = [] # Limpiar la lista de la hora específica
            
            if self.select_horas or self.fecha_seleccionada:
                # Convertir resultado (lista de listas/objetos) a lista de tuplas
                res = [tuple(row) for row in resultado]
                
                horarios_procesados = [] # Lista temporal para la hora seleccionada
                for r in res:
                    lista_r = list(r)  # Convertir la tupla a lista para modificar

                    # 4.1. Formatear nombre del docente
                    # r[1] es el nombre completo
                    nombres = r[1].split()  # Dividir el nombre completo
                    if len(nombres) >= 2:
                        lista_r[1] = f"{nombres[0]} {nombres[1]}"  # Acorta "Nombre ApellidoP ApellidoM" a "Nombre ApellidoP"
                    
                    # 4.2. Convertir la hora de la BD
                    # r[6] es el campo de la hora (timedelta)
                    hora_validar = self.convertir_a_hora_str(lista_r[6])

                    # 4.3. Poblar los diccionarios de la rejilla (TODAS las horas)
                    # r[0] es el nombre del salón
                    if r[0] in self.salones_primer_nivel:
                        # Obtener el índice (columna) que le corresponde en la rejilla
                        idx = self.salones_primer_nivel.index(r[0])
                        # (Manejo de seguridad por si la hora no estuviera en el dict)
                        if hora_validar not in self.horario_dict_1:
                            self.horario_dict_1[hora_validar] = [() for _ in self.salones_primer_nivel]
                        # Asignar los datos de la clase a su celda [hora][salon]
                        self.horario_dict_1[hora_validar][idx] = tuple(lista_r)
                    
                    if r[0] in self.salones_segundo_nivel:
                        idx = self.salones_segundo_nivel.index(r[0])
                        if hora_validar not in self.horario_dict_2:
                            self.horario_dict_2[hora_validar] = [() for _ in self.salones_segundo_nivel]
                        self.horario_dict_2[hora_validar][idx] = tuple(lista_r)

                    # 4.4. Filtrar por la hora seleccionada por el usuario
                    if hora_validar == self.select_horas:
                        
                        # Marcar el salón como ocupado en esta hora específica
                        if r[0] in self.salones_informacion:
                            self.salones_informacion[r[0]] = True
                        
                        # Añadir a la lista de horarios de la hora específica
                        horarios_procesados.append(tuple(lista_r))  # Convertir de vuelta a tupla

                # Actualizar la variable de estado principal
                self.lista_horarios = horarios_procesados

        # 5. Asegurar que la lista no esté vacía (para la UI)
        if not self.lista_horarios:
            # Si no hay clases en esta hora, añadir un marcador "NONE"
            # Esto evita que la UI falle si espera una lista con elementos.
            self.lista_horarios.append(tuple(["NONE"]))
