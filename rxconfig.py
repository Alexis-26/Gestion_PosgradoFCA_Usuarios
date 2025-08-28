import reflex as rx
import os

config = rx.Config(
    app_name="Gestion_PosgradoFCA_Usuario",
    # Puerto del frontend solo cuando corres en local
    frontend_port=int(os.getenv("FRONTEND_PORT", 3000)),

    # Railway te pasa un puerto dinámico en la variable PORT
    backend_port=int(os.getenv("PORT", 8000)),

    # URL de la base de datos (en Railway la defines en variables)
    db_url=os.getenv("DB_URL", "mysql+pymysql://root:password@localhost:3306/Gestion_PosgradoDB"),

    # URL del backend (para API)
    api_url=os.getenv("API_URL", "http://localhost:8000"),
)