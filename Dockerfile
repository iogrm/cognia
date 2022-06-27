FROM python:3.9
LABEL MAINTAINER="Amir Mohammad Mehri | https://myme.ir"

ENV PYTHONUNBUFFERED 1
RUN mkdir /cognia
WORKDIR /cognia
COPY . /cognia

ADD requirements/requirements.txt /cognia
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "cognia", "--bind", ":8000", "cognia.wsgi:application"]