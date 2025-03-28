import reflex as rx

class AppConfig(rx.Config):
    pass

config = AppConfig(
    app_name="Creyente",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    api_url="creyente-production.up.railway.app",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://creyente.vercel.app",
        "https://jcqsoft.com/creyente",
    ],
)