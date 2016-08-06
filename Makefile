dev: requirements requirements-dev

requirements:
	pip install -r requirements/requirements.txt

requirements-dev:
	pip install -r requiremente/requirements-dev.txt

freeze:
	pip freeze | diff requirements/requirements-dev.txt - | grep ">" | awk {'print $$2'} > requirements/requirements.txt

freeze-dev:
	pip freeze | diff requirements/requirements.txt - | grep ">" | awk {'print $$2'} > requirements/requirements-dev.txt
