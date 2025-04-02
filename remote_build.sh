cd Documents/Creyente
python -m venv .venvcreyente
source .venvcreyente/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 

# Export frontend
reflex export --frontend-only --no-zip [(3)](https://reflex.dev/docs/hosting/self-hosting)

# Si necesitas el archivo zip en lugar de los archivos estáticos:
# reflex export --frontend-only

# Si necesitas ambos frontend y backend:
# reflex export

deactivate