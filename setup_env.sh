#!bin/bash

python3 -m venv pdf &&
source pdf/bin/activate &&
pip install -r requirements.txt &&
deactivate