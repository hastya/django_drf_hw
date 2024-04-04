FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /django_drf_hw

COPY ./requirements.txt /django_drf_hw/

RUN pip install -r /django_drf_hw/requirements.txt

COPY . .

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
