import reflex as rx

class AppConfig(rx.Config):
    pass

config = AppConfig(
    app_name="Creyente",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    api_url="https://creyente.onrender.com",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://creyente.vercel.app",
        "https://jcqsoft.com/creyente",
    ],
)