import reflex as rx

config = rx.Config(
    app_name="Creyente",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://creyente.vercel.app"
    ],
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)