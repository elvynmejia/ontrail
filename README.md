# run app with
FLASK_APP=app.py flask run

# Save requirements
pip freeze > requirements.txt

# install dependencies
pip install -r requirements.txt

# run tests
PYTHONPATH=. py.test