import reflex as rx

config = rx.Config(
    app_name="Creyente",
    cors_allowed_origins=[
        "http://localhost:3000",
        "creyentes.vercel.app"
    ]
)