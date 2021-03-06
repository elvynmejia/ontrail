.PHONY: install
install:
	python3.6 -m venv venv
	. venv/bin/activate
	venv/bin/pip install -r requirements.txt

.PHONY: run
run:
	venv/bin/flask run --host "0.0.0.0"

.PHONY: shell
shell:
		venv/bin/flask shell

.PHONY: dev-db
dev-db:
	mysql -u root -proot -e "DROP DATABASE IF EXISTS ontrail_dev;"
	mysql -u root -proot -e "CREATE DATABASE IF NOT EXISTS ontrail_dev;"

.PHONY: test-db
test-db:
	mysql -u root -proot -e "DROP DATABASE IF EXISTS ontrail_test;"
	mysql -u root -proot -e "CREATE DATABASE IF NOT EXISTS ontrail_test;"

.PHONY: seed
seed:
	venv/bin/flask db upgrade
	venv/bin/flask seed create

.PHONY: clean
clean:
	mysql -u root -proot -e "DROP DATABASE IF EXISTS ontrail_dev;"
	mysql -u root -proot -e "DROP DATABASE IF EXISTS ontrail_test;"

.PHONY: test
test: test-db
	PYTHONPATH=. venv/bin/pytest
