# run app with
flask run --host "0.0.0.0"

# Save requirements
pip freeze > requirements.txt

# setup and install dependencies
$ python3.6 -m venv venv
$ pip install -r requirements.txt
$ source venv/bin/activate

# run tests
py.test
