FROM python:3.11.2-slim-bullseye

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY ./requirements.txt /requirements.txt

RUN pip install -U pip && \
    pip install --no-cache-dir --prefer-binary -r /requirements.txt

WORKDIR /mysite

COPY ./mysite /mysite

CMD ["python", "manage.py", "runserver"]