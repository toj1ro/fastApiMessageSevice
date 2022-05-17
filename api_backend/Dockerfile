FROM python:3.9.7
# set work directory
WORKDIR /usr/src/api_backend
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
# copy project
COPY . /usr/src/api_backend

EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "80"]