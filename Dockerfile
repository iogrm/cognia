FROM python:3.9
LABEL MAINTAINER="Amir Mohammad Mehri | https://myme.ir"

ENV PYTHONUNBUFFERED 1
RUN mkdir /uniform
WORKDIR /uniform
COPY . /uniform

ADD requirements/requirements.txt /uniform
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "uniform", "--bind", ":8000", "uniform.wsgi:application"]