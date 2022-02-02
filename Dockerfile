FROM python:2.7.18-stretch

WORKDIR /usr/src/app
COPY . .
RUN make install
RUN python manage.py migrate
RUN python manage.py seed

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
