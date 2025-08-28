import reflex as rx

config = rx.Config(
    app_name="Gestion_PosgradoFCA_Usuario",
    telemetry_enabled=False,
    frontend_port=3000,
    backend_port=8000,
    db_url="mysql+pymysql://root:GWqLlujpGEFqvQnhLspoIldtXyFDlZxm@autorack.proxy.rlwy.net:31857/Gestion_PosgradoDB",
    api_url="https://gestionposgradofcausuarios-production.up.railway.app"
)