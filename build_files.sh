#!/bin/bash
set -e

echo "BUILD START"

# Instale as dependências Python
pip install -r requirements.txt

# Execute o collectstatic do Django
python3 APP_API/manage.py collectstatic

echo "BUILD END"
