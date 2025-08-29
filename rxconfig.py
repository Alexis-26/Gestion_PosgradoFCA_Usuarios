import reflex as rx
import os

config = rx.Config(
    app_name="Gestion_PosgradoFCA_Usuario",

    # Y ESTE ES OPCIONAL (PRUEBA)
    # Puerto del frontend solo cuando corres en local
    frontend_port=int(os.getenv("FRONTEND_PORT", 3000)),

    # EL PORT DEBE DE SER EL MISMO QUE LA API PUBLICA
    # Railway te pasa un puerto dinámico en la variable PORT
    backend_port=int(os.environ.get("PORT", 8000)),

    # URL de la base de datos (en Railway la defines en variables)
    db_url=os.getenv("DB_URL", "mysql+pymysql://root:password@localhost:3306/Gestion_PosgradoDB"), # NECESARIO ACTIVAR ANTES DE SUBIR A HOST
   
   # ESTA ES LA BD EN SERVIDOR PERO ESTA EN VARIABLE DE ENTORNO
   # db_url=("mysql+pymysql://root:GWqLlujpGEFqvQnhLspoIldtXyFDlZxm@autorack.proxy.rlwy.net:31857/Gestion_PosgradoDB"),
    
    # URL del backend (para API)
    # ESTO DEBE APUNTAR A RAILWAY CUANDO SE EXPORTE EL FRONTED
    api_url=os.getenv("API_URL", "https://gestionposgradofcausuarios-production.up.railway.app"), # NECESARIO ACTIVAR ANTES DE SUBIR A HOST

    # Esto no se sabe si realmente funciona (PROBAR)
    # # Permitir que el frontend en Vercel se conecte vía WebSocket
    allowed_hosts=[
        "frontend-gpfca-usuarios.vercel.app" # NECESARIO ACTIVAR ANTES DE SUBIR A HOST
    ],
)
# SE DEBE DE UTILIZAR EL DOCKERFILE QUE SE ENCUENTRA AQUI PARA SUBIR EL BACKEND