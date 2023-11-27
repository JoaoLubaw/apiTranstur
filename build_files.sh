#!/bin/bash
set -e

echo "BUILD START"

# Instale as dependências Python
pip install -r requirements.txt

# Execute o collectstatic do Django
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"
