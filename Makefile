.PHONY: install
install:
	python3.6 -m venv venv
	. venv/bin/activate
	venv/bin/pip install -r requirements.txt

.PHONY: run
run: 
	venv/bin/flask run --host "0.0.0.0"

.PHONY: seed
seed:
	venv/bin/flask seed create

.PHONY: clean
clean:
	@echo "add commands to clean up venv and db"


