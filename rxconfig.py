import reflex as rx

class AppConfig(rx.Config):
    pass

config = AppConfig(
    app_name="Creyente",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://creyente.vercel.app",
        "https://jcqsoft.com/creyente",
    ],
    frontend_packages=[
        "swiper"
    ],
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)