#!/bin/bash
set -e

echo "BUILD START"

cd APP_API

# Instale as dependências Python
pip install -r requirements.txt

# Execute o collectstatic do Django
python3 manage.py collectstatic

echo "BUILD END"
