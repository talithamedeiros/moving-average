FROM python:3.9
LABEL maintainer Talitha Medeiros <medeirostalitha@gmail.com>

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev libffi-dev git --no-install-recommends

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /code

EXPOSE 8000

CMD /code/manage.py runserver 0.0.0.0:8000