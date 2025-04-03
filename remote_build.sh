#!/bin/bash
cd Documents/Creyente
python -m venv .venvcreyente
source .venvcreyente/bin/activate
pip install --upgrade pip
pip install -r requirements.txt 
rm -rf public
reflex init
reflex export --frontend-only --no-zip
mkdir -p public
cp -r .web/_static/* public/
deactivate