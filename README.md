# setup and install dependencies
`python3.6 -m venv venv` # creates a virtual environment
`source venv/bin/activate` # activates virtual environment
`venv/bin/flask pip install -r requirements.txt` # install requirements

# Install and save a package
`venv/bin/flask pip install numpy` # for example
`venv/bin/flask pip freeze > requirements.txt`

# run app with
`venv/bin/flask run --host "0.0.0.0"`


# run tests
py.test
