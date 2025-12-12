from sqlalchemy import text  # Importa la función text para las operaciones SQL
import reflex as rx

class MYSQLDB(rx.Base):
    """
    Clase de utilidad para interactuar con la base de datos MySQL.

    Actúa como una capa de acceso a datos (DAO) que centraliza
    la ejecución de procedimientos almacenados (stored procedures).

    Nota: Esta clase hereda de rx.Base para la integración básica con
    el sistema de tipos de Reflex, pero no es un rx.Model (tabla)
    ni un rx.State (estado de la UI).
    """

    def consulta_horarios(self):
        """
        Ejecuta el Stored Procedure 'sp_ConsultarHorarios'.

        Se espera que este SP devuelva una lista de todos los
        horarios generales.

        Returns:
            DbResult: Una lista de tuplas (filas) con los resultados
            de la consulta, o None si ocurre un error de base de datos.
        """
        try:
            with rx.session() as session:
                resultado = session.exec(
                    text("CALL sp_ConsultarHorarios()")
                ).fetchall()
                # .fetchall() devuelve una lista de objetos Row,
                # que se comportan como tuplas
                return resultado
        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}")

    def consulta_asignacion_fecha(self, fecha:str):
        """
        Ejecuta el Stored Procedure 'ConsultarAsigFecha' con una fecha.

        Se espera que este SP devuelva las asignaciones de horarios
        para la fecha específica proporcionada.

        Args:
            fecha (str): La fecha a consultar.

        Returns:
            DbResult: Una lista de tuplas (filas) con las asignaciones
            para esa fecha, o None si ocurre un error de base de datos.
        """
        try:
            with rx.session() as session:
                # Usar 'params' es la forma segura de pasar argumentos
                # a consultas SQL, previniendo inyección SQL.
                resultado = session.exec(
                    text("CALL ConsultarAsigFecha(:fecha)"),
                    params={"fecha":fecha}
                ).fetchall()
                return resultado
        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}")