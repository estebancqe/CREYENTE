import reflex as rx

config = rx.Config(
    app_name="Creyente",
    db_url="sqlite:///reflex.db",
    api_url="https://creyente-web.up.railway.app",
    cors_allowed_origins=[
        "http://localhost:3000", 
        "https://creyente.vercel.app",
        "https://jcqsoft.com/creyente"],
)