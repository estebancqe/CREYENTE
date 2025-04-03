cd Documents/Creyente
python -m venv .venvcreyente
source .venvcreyente/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
rm -rf public
reflex init
API_URL=https://creyente.onrender.com reflex export --frontend-only --no-zip [(1)](https://reflex.dev/docs/hosting/self-hosting)
mkdir -p public
cp -r .web/_static/* public/ [(1)](https://reflex.dev/docs/hosting/self-hosting)
deactivate