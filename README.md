python -m venv myvenv

myvenv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
