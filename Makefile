.PHONY: install run lint test
deafult: install

install:
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py seed

run:
	python manage.py migrate
	python manage.py runserver

lint:
	pylint app pygoat

test:
	coverage run manage.py test app
	coverage report
