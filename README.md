# run app with
flask run

# Save requirements
pip freeze > requirements.txt

# install dependencies
pip install -r requirements.txt

# run tests
PYTHONPATH=. py.test
