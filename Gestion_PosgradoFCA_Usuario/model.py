import reflex as rx
from sqlalchemy import text  # Importa la función text esto es porque esta,os consultando de manera cruda

class MYSQLDB(rx.Base):
    def consulta_horarios(self):
        try:
            with rx.session() as session:
                resultado = session.exec(
                    text("CALL sp_ConsultarHorarios()")
                ).fetchall()
                return resultado
        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}")

    def consulta_asignacion_fecha(self, fecha:str):
        try:
            with rx.session() as session:
                resultado = session.exec(
                    text("CALL ConsultarAsigFecha(:fecha)"),
                    params={"fecha":fecha}
                ).fetchall()
                return resultado
        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}")