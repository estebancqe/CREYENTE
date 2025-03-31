import reflex as rx

config = rx.Config(
    app_name="Creyente",
    # Para producción, usa una base de datos PostgreSQL
    db_url="postgresql://user:password@localhost:5432/creyente_db",  
    api_url="https://creyente.onrender.com",
    # Asegúrate que los CORS estén correctamente configurados
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://creyente.vercel.app",
        "https://jcqsoft.com/creyente"
    ],
    # Configuración para producción
    frontend_port=3000,
    backend_port=8000
)