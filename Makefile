

make:
	python manage.py makemigrations
migrate:
	python manage.py migrate

run:
	python manage.py runserver

create_superuser:
	python manage.py createsuperuser