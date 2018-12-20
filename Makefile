.PHONY: install, lint, test, travis
deafult: install

install:
	pip install -r requirements.txt

run:
	python manage.py migrate
	python manage.py runserver

lint:
	pylint app pygoat

test:
	python manage.py test app

travis: intsall lint test
