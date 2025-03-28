cd Documents/Creyente
python -m venv .venvcreyente
source .venvcreyente/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
rm -rf public
reflex init
API_URL=https://creyente.onrender.com reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate